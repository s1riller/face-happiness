<template>

  <header class="p-3 bg-discord-blue gg-sans">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
          <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"></use></svg>
        </a>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <router-link to="/" class="nav-link px-2 text-white">Домой</router-link>
          <router-link to="/Testing" class="nav-link px-2 text-white">Тестирование</router-link>
          <router-link to="/Performance" class="nav-link px-2 text-white">Эффективность</router-link>
          <router-link to="/Statistic" class="nav-link px-2 text-white">Статистика</router-link>
          <li><a href="#" class="nav-link px-2 text-white">About</a></li>
        </ul>

        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
          <input type="search" class="form-control form-control-dark text-bg-white" placeholder="Поиск" aria-label="Search">
        </form>

        <div v-if="token==='null'" class="text-end">
          <!-- Кнопка-триггер модального окна регистрации -->
          <button type="button" class="btn bg-light rounded-5 " data-bs-toggle="modal" data-bs-target="#signupModal">
            Нужна учетная запись?
          </button>

          <button type="button" class="btn btn-outline-light me-2 rounded-5" data-bs-toggle="modal" data-bs-target="#signinModal">
            Войти
          </button>

        </div>
        <button v-if="token!=='null'" type="button" @click="Logout" class="btn btn-outline-light me-2 rounded-5" data-bs-toggle="modal" data-bs-target="#signinModal">
          Выйти

        </button>
      </div>
    </div>

    <!-- Модальное окно регистрации -->
    <form @submit.prevent="Signup(username,password,birthday)"  class="modal fade blur" id="signupModal" tabindex="-1" aria-labelledby="signupModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content p-4 mb-2 bg-white">
          <div class="modal-header">
            <h5 class="modal-title text-black" id="signupModalLabel">Рады видеть вас!</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <label class="text-black mb-1">Адрес электронной почты <span class=text-discord-red>*</span></label>
              <input type="text" v-model="username" class="form-control" required />
            </div>

            <div class="form-group pt-2">
              <label class="text-black mb-1">Пароль <span class=text-discord-red>*</span></label>
              <input type="password" v-model="password" class="form-control" required />
            </div>

            <div class="form-group pt-2">
              <label class="text-black mb-1">День рождения <span class=text-discord-red>*</span></label>
              <input type="date" class="form-control" v-model="birthday" name="birthday" placeholder="Дата" required />
            </div>


          </div>


          <div v-if="getError==='Произошла ошибка при регистрации. Пожалуйста, проверьте данные и повторите попытку.'" class="alert alert-danger" role="alert">
            {{ getError }}
          </div>
          <div v-if="getError==='Поздравляем! Успешная регистрация!'" class="alert alert-success" role="alert">
            {{ getError }}
          </div>
          <div class="modal-footer d-flex justify-content-center">
            <button type="submit" class="btn btn-success text-white rounded-5">Зарегистрироваться</button>
          </div>
        </div>
      </div>
    </form>


    <!-- Модальное окно входа -->
    <form @submit.prevent="Login(username,password)" class="modal fade blur" id="signinModal" tabindex="-1" aria-labelledby="signinModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content p-3 mb-2">
          <div class="modal-header">
            <h5 class="modal-title" id="signinModalLabel">С возвращением!</h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Закрыть"></button>
          </div>

          <div class="modal-body">
            <div class="form-group pt-2">
              <label class="text mb-1">Адрес электронной почты <span class=text-discord-red>*</span></label>
              <input v-model="username" type="text" class="form-control"  autocomplete="username"/>
            </div>
            <div class="form-group pt-2">
              <label class="text mb-1">Пароль <span class=text-discord-red>*</span></label>
              <input v-model="password" type="password" class="form-control" autocomplete="current-password"/>
            </div>
          </div>

          <div v-if="getError==='Произошла ошибка при авторизации.'" class="alert alert-danger" role="alert">
            {{ getError }}
          </div>
          <div v-if="getError!=='Произошла ошибка при авторизации.'" class="alert alert-success" role="alert">
            {{ getError }}
          </div>

          <div class="modal-footer d-flex justify-content-between align-items-center">
            <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#signinModal">
              Забыл пароль
            </button>
            <button  type="submit" class="btn bg-discord-blue text-white rounded-5">Войти</button>

          </div>





        </div>
      </div>

    </form>

  </header>


</template>

<script>

import Calendar from "@/components/calendar.vue";
import "@/static/discord.css";
import axios from "axios";
import {mapActions, mapGetters, mapMutations} from "vuex";
export default {
  components: {Calendar},

  name: 'Navbar',
  data(){
    return{
      API_URL:'http://127.0.0.1:8000',
      token: localStorage.getItem('token'),
      username: '',
      password: '',
      birthday: '',
      isLoading: false
    }
  },

  methods: {
    ...mapActions(['SignupStore','LogoutStore','fetchUserDataStore','LoginStore']),

    Logout(){
      this.LogoutStore()
    },
    Signup() {
      this.SignupStore({
        username: this.username,
        password: this.password,
        birth_date: this.birthday,
      })
    },
    Login() {
      this.LoginStore({
        username: this.username,
        password: this.password,
        birth_date: this.birthday,
      })
    }
  },

  computed: {
    ...mapGetters(['getError','getUserName']),

  },
  created(){
    if(localStorage.getItem('token')===null){
    this.fetchUserDataStore()}
    // console.log('Username from getter:', this.getUserName);
    this.username = this.getUserName;
    // Set the username from the getter

  },


}

</script>

<style scoped>
.blur{
  backdrop-filter: blur(2px);
}
.bg-discord-blue{
  background-color: #5865F2;
}
.gg-sans{
  font-family: "gg sans", sans-serif;
}
.bg-discord-black{
  background-color: #23272A;
}
.text-discord-red{
  color: #ED4245;
}

.form-control-color-discord-black:focus{
  width: 100%;
  height: 48px;
  border: 2px solid #3626a7;
  background: rgba(54,38,167,0.32);
  border-radius: 8px;
  text-align: center;
  color: #fff;
  font-size: 24px;
}

.form-control-color-discord-black{
  width: 100%;
  height: 48px;
  border: 2px solid #3626a7;
  background: rgba(54,38,167,0.32);
  border-radius: 8px;
  text-align: center;
  color: #fff;
  font-size: 24px;
}
</style>