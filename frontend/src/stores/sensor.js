import { defineStore } from "pinia";

export const useSensorStore = defineStore({
    id: 'sensor',
    state: () => ({
        data: {},
    }),
    getters: {

    },
    actions: {
        async fetchData() {
            this.data = await fetch("https://greenhouse-monitor.herokuapp.com/api/test")
                            .then(resp => {
                                if(resp.status >= 400){
                                    throw Error("Cannot fetch data");
                                }
                                return resp.json()
                            })
                            .then(data => data)
        }
    }
})