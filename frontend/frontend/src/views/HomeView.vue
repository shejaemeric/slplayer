<template>
    <div class="container">
        <div class="center">

                <div class="pulse-blue" v-if="!recording">
                    <button  @click="startRecording">Start Recording</button>
                </div>

                <div class="pulse-red" v-if="recording">
                    <button  @click="stopRecording">Stop Recording</button>
                </div>

        </div>
    </div>
</template>

<script>
import RecordRTC from 'recordrtc';

export default {
    name: "HomeView",
    data(){
        return {
            recording:false,
            recorder:null,
        }
    },
    methods:{
        startRecording (){
            // Get recording stream of user device/browser
            const stream = navigator.mediaDevices.getUserMedia({audio: true})
            .then(stream => {
                //start recording
                this.recorder = new RecordRTC(stream,{
                    type:'audio',
                    mimeType:'audio/mp3'
                });
                this.recorder.startRecording();
            });
            this.recording = true;

        },

        async sendAudio(audioBlob){
            const axios = require("axios");

            //add blob to form
            const data = new FormData();
            data.append("upload_file",audioBlob);

            //request option
            const options = {
                method: 'POST',
                url: 'https://shazam-song-recognizer.p.rapidapi.com/recognize',
                headers: {
                    'X-RapidAPI-Key': '291956e6a0msh45c40c5ab4a881ep1bea65jsn220317b787e4',
                    'X-RapidAPI-Host': 'shazam-song-recognizer.p.rapidapi.com',
                },
                data: data
            };
            try{
                const response = await axios.request(options)
                console.log(response.data.result.subtitle);
                console.log(response.data.result.title);

            }catch(error){
                console.log(error)
            }
        },

        async stopRecording (){

            this.recorder.stopRecording( ()=>{
                //get the recorder audio as a blob
                const audioBlob = this.recorder.getBlob();
                // send audio
                this.sendAudio(audioBlob);
            })
            this.recording = false;
        }
    }
  }
</script>

<style scoped>
    .container{
        width: 20%;
        height: 300px;
        background-color: #ffffff00;
    }
    .center{
        transform: translate(-50%, -50%);
        margin-top: 8rem;
    }

    .pulse-red{
        width: 100px;
        height: 100px;
        background: #e41e1e;
        border-radius: 50%;
        color: #FFF;
        font-size: 20px;
        text-align: center;
        line-height: 100px;
        font-family: sans-serif;
        text-transform: uppercase;
        animation: animate-pulse-red 3s linear infinite;
        cursor: pointer
    }
    .pulse-blue{
        width: 100px;
        height: 100px;
        background: #4aa7ff;
        border-radius: 50%;
        color: #FFF;
        font-size: 20px;
        text-align: center;
        line-height: 100px;
        font-family: sans-serif;
        text-transform: uppercase;
        animation: animate-pulse-blue 3s linear infinite;
        cursor: pointer
    }
    @keyframes animate-pulse-red{
        0%{
            box-shadow: 0 0 0 0 #e41e1eb3,  0 0 0 0 #e41e1eb3;
        }
        40%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 0 #e41e1eb3;
        }
        80%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }
        100%{
            box-shadow: 0 0 0 0 #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }

    }

    @keyframes animate-pulse-blue{
        0%{
            box-shadow: 0 0 0 0 #4aa7ffb3,  0 0 0 0 #4aaeffb3;
        }
        40%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 0 #4abdffb3;
        }
        80%{
            box-shadow: 0 0 0 50px #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }
        100%{
            box-shadow: 0 0 0 0 #ff6d4a00,  0 0 0 30px #ff6d4a00;
        }

    }

</style>
