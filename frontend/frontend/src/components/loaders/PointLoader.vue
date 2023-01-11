
<template>
    <div class="pulse-blue">
        <div class="dot-loader"></div>
        <div class="dot-loader dot-loader--2"></div>
        <div class="dot-loader dot-loader--3"></div>
    </div>
</template>

<style>
    .dot-loader {
        height: 20px;
        width: 20px;
        border-radius: 50%;
        background-color: #ffffff;
        position: relative;
        -webkit-animation: 1.2s grow ease-in-out infinite;
        animation: 1.2s grow ease-in-out infinite;
        margin:0px 3px 0px 7px !important;
    }

    .dot-loader--2 {
    -webkit-animation: 1.2s grow ease-in-out infinite 0.15555s;
    animation: 1.2s grow ease-in-out infinite 0.15555s;
    margin: 0 20px;
    }
    .dot-loader--3 {
    -webkit-animation: 1.2s grow ease-in-out infinite 0.3s;
    animation: 1.2s grow ease-in-out infinite 0.3s;
    }

    @keyframes grow {
        0%, 40%, 100% {
            -webkit-transform: scale(0);
                    transform: scale(0);
        }
        40% {
            -webkit-transform: scale(1);
                    transform: scale(1);
        }
    }
</style>

<script>
export default {
    name:"PointLoader",
}
</script>
