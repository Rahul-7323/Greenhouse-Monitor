<script>
import Gear from "./icons/Gear.vue"

export default {
    components: {
        Gear,
    },
    props: {
        isOn : Boolean,
    }
}

</script>


<template>  
<div class="flex flex-col justify-center align-middle bg-white rounded-lg p-3 w-1/4 md:gap-5 h-44 cool-bg">
    <div class="font-sans flex text-[#007C84] md:text-3xl justify-center">Water Pump</div>
    <div v-if="isOn" class=" flex flex-row bg-[#007C84] p-4 justify-between align-middle rounded-full w-8/12 self-center">
        <div class="mr-2 text-[#007C84]"><div class="rounded-full bg-white p-3 shadow-lg shadow-white"><Gear class="md:w-12 md:h-12"/></div></div>
        <div class="md:text-2xl ml-3 text-white font-bold flex flex-col justify-center">ON</div>
    </div>
    <div v-else class="flex flex-row bg-[#EAF3F4] p-4 justify-between align-middle rounded-full w-8/12 self-center">
        <div class="mr-2 md:text-2xl text-[#007C84] font-bold flex flex-col justify-center">OFF</div>
        <div class="text-white ml-3"><div class="rounded-full bg-[#007C84] p-3 shadow-lg shadow-[#007C84]"><Gear class="md:w-12 md:h-12"/></div></div>
    </div>
</div>
</template>