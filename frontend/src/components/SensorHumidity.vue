<script>
import Humidity from "./icons/Humidity.vue"

export default {
    components: {
        Humidity,
    },
    props: {
        humidity: Number
    }
}

</script>


<template>  
<div class="flex flex-col justify-center align-middle bg-white rounded-lg p-3 w-1/4 md:gap-5 h-44 cool-bg">
    <div class="font-sans flex text-[#007C84] md:text-3xl justify-center">Humidity</div>
    <div class="flex flex-row bg-[#EAF3F4] rounded-lg p-2 justify-center">
        <div class="mt-[10px] mr-2 text-[#007C84]"><Humidity class="md:w-12 md:h-12"/></div>
        <div class="md:text-6xl ml-3 text-[#00495F] font-bold">{{humidity}}%</div>
    </div>
</div>
</template>