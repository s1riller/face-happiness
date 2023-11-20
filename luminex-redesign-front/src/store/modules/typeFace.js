


export default {
    namespaced: true,
    actions: {
        async fetchTypeFaces({ commit }) {
            const res = await fetch("http://185.84.163.151:8000/api/skintypes/");
            const typeFaces = await res.json();

            commit('updateTypeFaces', typeFaces); // Обратите внимание на исправленное имя мутации
        },
    },
    mutations: {
        updateTypeFaces(state, typeFaces) {
            state.typeFace = typeFaces;
        },
    },
    state:{
        typeFace:[]
    },
    getters: {
        allTypeFaces(state) {
            return state.typeFace;
        },
    },


}