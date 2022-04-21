<script>
import { useSensorStore } from "../stores/sensor"
import SensorTemperature from "../components/SensorTemperature.vue";
import SensorMoisture from "../components/SensorMoisture.vue";
import SensorHumidity from "../components/SensorHumidity.vue";
import SensorAirVent from "../components/SensorAirVent.vue";
import SensorWaterPump from "../components/SensorWaterPump.vue";
import TheHeader from "../components/TheHeader.vue";


export default {
    components: {
    TheHeader,
    SensorHumidity,
    SensorTemperature,
    SensorMoisture,
    SensorAirVent,
    SensorWaterPump
},
    setup(){
        const SensorStore = useSensorStore();
        return {SensorStore};
    },
    data() {
        return {
            loadingBar: 0,
        }
    },
    computed: {
        data() {
            return this.SensorStore.data;
        }
    },
    mounted(){
        this.SensorStore.fetchData();
        setInterval(() => {
            this.loadingBar += 0.2;
            if(this.loadingBar > 100){
                this.loadingBar = 0;
            }
        },20)
        setInterval(() => {
            this.SensorStore.fetchData();
        },10000)
    }
}

</script>

<template>
<div class="w-screen bg-gray-200 h-3 fixed top-0">
    <div class="bg-blue-600 h-3 rounded-xl" :style="{ width: loadingBar+'%' }"></div>
</div>
<div class="p-5 flex flex-col gap-y-10">
    <TheHeader/>
    <div class="flex flex-row flex-wrap gap-10 justify-center">
        <SensorTemperature :temperature="data.temperature"/>
        <SensorMoisture :moisture="data.moisture"/>
        <SensorHumidity :humidity="data.humidity"/>
        <SensorAirVent :isOpen="data.air_vent"/>
        <SensorWaterPump :isOn="data.water_pump"/>
    </div>
</div>
</template>