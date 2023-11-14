<template>
  <body class="d-flex bg-discord-gray vh-100">
  <div class="container">
    <div class="row">
      <div class="mx-auto">
        <div class="block bg-discord-black text-white d-flex justify-content-center align-items-center vh-100">
          <!-- Кнопка-триггер модального окна -->
          <button type="button" class="btn btn-lg btn-light fw-bold" data-bs-toggle="modal" data-bs-target="#questionsModal">
            Начать
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Второе модальное окно -->
  <div class="modal fade" id="questionsModal" tabindex="-1" aria-labelledby="questionsModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">{{ currentQuestion.question }}</h1>
          <button v-if="!loading" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
        </div>
        <div class="modal-body">
          <div class="form-check" v-for="(answer, index) in currentQuestion.answers" :key="index">
            <input
                class="form-check-input"
                :type="currentQuestion.id === 1000 ? 'checkbox' : 'radio'"
                name="answerRadio"
                :value="answer.id"
                :id="'answerRadio_' + index"
                :checked="false"
                :defaultChecked="false"
            @change="saveAnswer(answer)"
            />
            <label class="form-check-label" :for="'answerRadio_' + index">{{ answer.text }}</label>
          </div>
        </div>
        <div class="modal-footer">
          <button v-if="!loading" type="button" class="btn btn-secondary" @click="prevQuestion">Назад</button>
          <button v-if="currentQuestionIndex !== (getQuestions.length - 1)" type="button" class="btn btn-primary" @click="nextQuestion">Далее</button>
          <button v-if="!loading && currentQuestionIndex === (getQuestions.length - 1)" class="btn btn-primary" type="button" @click="submitAnswers">Отправить результаты</button>
          <div v-if="loading" class="d-flex align-items-center">
            <div class="spinner-border text-primary" role="status">

            </div>
            <span class="ms-2">Мы анализируем ваши данные</span>
          </div>

        </div>

      </div>
    </div>
  </div>
  </body>
</template>

<style>
</style>

<script>
import "@/static/discord.css";
import { mapGetters } from 'vuex';
import axios from "axios";

export default {



  data() {
    return {
      currentQuestionIndex: 0,
      selectedAnswers: {},
      loading: false, // Инициализируйте состояние loading
    };
  },
  computed: {
    ...mapGetters(['getQuestions']),
    currentQuestion() {
      return this.getQuestions[this.currentQuestionIndex] || {};
    },
  },
  methods: {
    nextQuestion(answer) {
      // Переход к следующему вопросу
      if (this.currentQuestionIndex < this.getQuestions.length - 1) {
        this.currentQuestionIndex++;
        this.saveAnswer(answer);
      }
    },
    prevQuestion() {
      // Переход к предыдущему вопросу
      if (this.currentQuestionIndex > 0) {
        this.currentQuestionIndex--;
      }
    },
    async submitAnswers() {
      try {
        this.loading = true; // Установите loading в true перед началом загрузки

        // Запрос, чтобы получить id пользователя
        const profileResponse = await axios.get('http://127.0.0.1:8000/api/profile', {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        });
        const userId = profileResponse.data.id;

        // Фильтруем selectedAnswers, чтобы удалить null значения
        const cleanedAnswers = {};
        for (const key in this.selectedAnswers) {
          if (this.selectedAnswers[key] !== null) {
            cleanedAnswers[key] = this.selectedAnswers[key];
          }
        }

        const results = {
          user: userId, // Отправляем id пользователя
          answers: cleanedAnswers, // Отправляем выбранные ответы без null
        };

        const response = await axios.post('http://127.0.0.1:8000/api/user_test_results/', results, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        });
        await new Promise((resolve) => {
          setTimeout(resolve, 10000);
        });
        this.loading = false; // Завершите загрузку, установив loading в false
        this.$router.replace({ name: 'performance' });


        setTimeout(() => {
          window.location.reload();
        }, 100);
      } catch (error) {
        this.loading = false; // Установите loading в false в случае ошибки
        console.error(error);
      }
    },
    saveAnswer(answer) {
      if (answer && answer.id !== null) { // Проверяем, что answer существует и не является null
        // Проверяем, есть ли уже выбранные ответы для текущего вопроса
        if (!this.selectedAnswers[this.currentQuestion.question]) {
          // Если нет, создаем новый массив и добавляем в него ответ
          this.selectedAnswers[this.currentQuestion.question] = [answer.text];
        } else {
          // Если уже есть выбранные ответы, добавляем новый ответ в массив
          this.selectedAnswers[this.currentQuestion.question].push(answer.text);
        }
      }
    }


  },
  mounted() {
    this.$store.dispatch('fetchQuestions', localStorage.getItem('token'));
  },
};
</script>