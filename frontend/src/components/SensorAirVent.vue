<script>
import Door from "./icons/Door.vue"

export default {
    components: {
        Door,
    },
    props: {
        isOpen : Boolean
    }
}

</script>


<template>  
<div class="flex flex-col justify-center align-middle bg-white rounded-xl p-3 w-1/4 md:gap-5 h-44 cool-bg">
    <div class="font-sans flex text-[#007C84] md:text-3xl justify-center">Air Vent</div>
    <div v-if="isOpen" class=" flex flex-row bg-[#007C84] p-4 justify-between align-middle rounded-full w-9/12 self-center">
        <div class="mr-2 text-[#007C84]"><div class="rounded-full bg-white p-3 shadow-lg shadow-white"><Door class="md:w-12 md:h-12"/></div></div>
        <div class="md:text-2xl ml-3 text-white font-bold flex flex-col justify-center">OPEN</div>
    </div>
    <div v-else class="flex flex-row bg-[#EAF3F4] p-4 justify-between align-middle rounded-full w-9/12 self-center">
        <div class="mr-2 md:text-2xl text-[#007C84] font-bold flex flex-col justify-center">CLOSED</div>
        <div class="text-white ml-3"><div class="rounded-full bg-[#007C84] p-3 shadow-lg shadow-[#007C84]"><Door class="md:w-12 md:h-12"/></div></div>
    </div>
</div>
</template>