<script>
import { useSensorStore } from "../stores/sensor"


export default {
    setup(){
        const SensorStore = useSensorStore();
        return {SensorStore};
    },
    computed: {
        data() {
            return this.SensorStore.data;
        }
    },
    mounted(){
        this.SensorStore.fetchData();
    }
}

</script>

<template>
<div class="font-mono text-lg">Dashboard</div>
<ul>
    <li v-for="article in data">{{ article.title }} : {{ article.content }}</li>
</ul>
</template>