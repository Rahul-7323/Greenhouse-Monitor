<script>
import ThermometerIcon from "../components/icons/ThermometerHalf.vue";

export default {
    components: {
        ThermometerIcon,
    },
    props: {
        temperature: Number
    }
}

</script>


<template>
<div class="flex flex-col justify-center align-middle bg-white rounded-lg p-3 w-1/4 md:gap-5 h-44 cool-bg">
    <div class="font-sans flex text-[#007C84] md:text-3xl justify-center">Temperature</div>
    <div class="flex flex-row bg-[#EAF3F4] rounded-lg p-2 justify-center">
        <div class="mt-[6px] text-[#007C84]"><ThermometerIcon class="md:w-14 md:h-14"/></div>
        <div class="md:text-6xl ml-3 text-[#00495F] font-bold">{{temperature}}&deg;C</div>
    </div>
</div>
</template>