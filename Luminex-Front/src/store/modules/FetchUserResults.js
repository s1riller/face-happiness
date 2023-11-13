// store.js
import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";


export default({
    state: {
        id: null,
        userTestResults: []
    },
    getters: {
        getUserName: (state) => state.user.username,
        getUserId: (state) => state.id,
        getUserTestResults: (state) => state.userTestResults,
    },
    mutations: {
        setId(state, id) {
            state.id = id;
        },
        setUserTestResults(state, results) {
            state.userTestResults = results;
        },
        filterUserTestResults(state) {
            state.userTestResults = state.userTestResults.filter(result => result.user === state.id);
        }
    },
    actions: {
        async fetchUserTestResults(context) {
            try {
                // Запрос на получение ID пользователя
                const responseProfile = await axios.get('http://127.0.0.1:8000/api/profile', {
                    headers: {
                        'Authorization': `Token ${localStorage.getItem('token')}`,
                    },
                });

                if (responseProfile.data) {
                    context.commit('setId', responseProfile.data.id);
                }

                // Запрос на получение всех результатов
                const responseResults = await axios.get('http://127.0.0.1:8000/api/usertestresults/', {
                    headers: {
                        'Authorization': `Token ${localStorage.getItem('token')}`,
                    }
                });

                context.commit('setUserTestResults', responseResults.data);

                // Фильтрация результатов по ID пользователя
                context.commit('filterUserTestResults');
            } catch (error) {
                console.error(error);
            }
        }
    }
});
