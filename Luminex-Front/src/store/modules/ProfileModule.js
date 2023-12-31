// profileModule.js

import axios from 'axios';
import data from "bootstrap/js/src/dom/data";

export default {
    state:{
        user: {
            username: '', // Имя пользователя
            birth_date: '', // Дата рождения пользователя
        },
        error: null, // Ошибка, если есть
    },

   getters: {
       getUserName(state) {
           return state.user.username;
       },
    },

   mutations: {
        setUserData(state, userData) {
            state.user.username = userData.username;
            state.user.birth_date = userData.birth_date;
        },

    },

     actions: {
        async fetchUserDataStore({commit}) {
            try {
                const response = await axios.get('http://127.0.0.1:8000/api/profile', {
                    headers: {
                        'Authorization': `Token ${localStorage.getItem('token')}`
                    }
                });
                // console.log(response.data)
                if (response.data) {
                    // console.log(response.data)
                    commit('setUserData',response.data)
                }
            } catch (error) {
                console.error(error);

            }
        },
    }
}