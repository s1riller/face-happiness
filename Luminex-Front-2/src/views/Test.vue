<template>
  <body class="d-flex bg-light vh-100">
  <div class="container">
    <div class="row">
      <div class="mx-auto">
        <div class="card bg-light text-dark d-flex justify-content-center align-items-center vh-100">
          <div v-if="currentQuestion" class="card-body">
            <h5 class="card-title text-dark text-center">{{ currentQuestion.title }}</h5>
            <div class="d-flex flex-row justify-content-around">
              <div v-for="image in currentQuestion.images" :key="image.value" class="mr-3">
                <button type="button" class="btn" @click="selectAnswer(image.value)">
                  <img :src="image.src" alt="" class="img-fluid rounded" style="width: 230px; height: 300px;" />
                  <h5 class="mt-2">{{ image.text }}</h5>
                </button>
              </div>
            </div>
          </div>
          <div v-else class="card-body">
            <p class="card-text">No more questions.</p>
            <p class="card-text">Выбранные ответы: {{ formatSelectedAnswers }}</p>
            <div v-if="serverResponse">
              <p class="card-text">Ответ сервера: {{ serverResponse }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
import "@/static/discord.css";
import { mapGetters } from 'vuex';
import axios from "axios";
const cheerio = require('cheerio');
export default {
  data() {
    return {
      currentQuestionIndex: 0,
      selectedAnswers: {},
      loading: false,
      serverResponse: null, // Добавленная переменная для хранения ответа сервера

      questions: [
        {
          "title": "1. Какие у вас ощущения после умывания",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/1a.jpg?v=1",
              "text": "Комфортные, ничего не беспокоит"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/1b.jpg?v=1",
              "text": "Есть дискомфорт: ощущаю стянутость"
            }
          ]
        },
        {
          "title": "2. Как ведет себя кожа в течение дня?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/2a.jpg?v=1",
              "text": "Не очень хорошо. Жирный блеск на всем лице возникает через 2–3 часа после умывания"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/2b.jpg?v=1",
              "text": "Хорошо. Жирный блеск может появиться только ближе к середине дня или к вечеру"
            },
            {
              "value": "c",
              "src": "https://aravia.ru/skin-test/img/questions/2c.jpg?v=1",
              "text": "Возникает чувство дискомфорта. Ближе к полудню кожу стягивает, хочется нанести крем"
            },
            {
              "value": "d",
              "src": "https://aravia.ru/skin-test/img/questions/2d.jpg?v=1",
              "text": "Зависит от зоны. В течение дня в Т-зоне появляется жирный блеск, периферию может стягивать"
            }
          ]
        },
        {
          "title": "3. КАКИЕ НЕСОВЕРШЕНСТВА БЕСПОКОЯТ ВАС БОЛЬШЕ ВСЕГО?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/3a.jpg?v=1",
              "text": "Черные точки — присутствуют постоянно, в основном в Т-зоне"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/3b.jpg?v=1",
              "text": "Иногда беспокоят единичные воспаления"
            },
            {
              "value": "c",
              "src": "https://aravia.ru/skin-test/img/questions/3c.jpg?v=1",
              "text": "Не беспокоят, кожа выглядит чистой и ровной"
            },
            {
              "value": "d",
              "src": "https://aravia.ru/skin-test/img/questions/3d.jpg?v=1",
              "text": "Сильно беспокоят частые воспаления в разных участках лица"
            }
          ]
        },
        {
          "title": "4. Как Вы оцениваете состояние пор?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/4b.jpg?v=1",
              "text": "Не расширены"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/4a.jpg?v=1",
              "text": "Расширены"
            },
            {
              "value": "c",
              "src": "https://aravia.ru/skin-test/img/questions/4c.jpg?v=1",
              "text": "Расширены в Т-зоне"
            }
          ]
        },
        {
          "title": "5. Присутствуют ли элементы постакне",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/5a.jpg?v=1",
              "text": "Да"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/5b.jpg?v=1",
              "text": "Нет"
            }
          ]
        },
        {
          "title": "6. ПРОВЕДИТЕ ЭКСПРЕСС-ТЕСТ НА УПРУГОСТЬ КОЖИ",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/6a.jpg?v=1",
              "text": "Кожу сложно ущипнуть, складка не образуется"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/6b.jpg?v=1",
              "text": "Складка образуется, но сразу расправляется"
            },
            {
              "value": "c",
              "src": "https://aravia.ru/skin-test/img/questions/6c.jpg?v=1",
              "text": "Складка образуется легко и расправляется медленно"
            }
          ]
        },
        {
          "title": "7. РАССЛАБЬТЕ МЫШЦЫ ЛИЦА И ПОСМОТРИТЕ В ЗЕРКАЛО — ВИДИТЕ ЛИ ВЫ МОРЩИНЫ?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/7a.jpg?v=1",
              "text": "Нет выраженных морщин"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/7b.jpg?v=1",
              "text": "Есть немного, в основном мимические"
            },
            {
              "value": "c",
              "src": "https://aravia.ru/skin-test/img/questions/7c.jpg?v=1",
              "text": "Да, хорошо вижу: мелкие и крупные"
            }
          ]
        },
        {
          "title": "8. ОЦЕНИТЕ СОСТОЯНИЕ КОЖИ ВОКРУГ ГЛАЗ. ЧТО ВАС БЕСПОКОИТ БОЛЬШЕ ВСЕГО?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/8a.jpg?v=1",
              "text": "Частые отеки, мешки под глазами"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/8b.jpg?v=1",
              "text": "Темные круги под глазами"
            },
            {
              "value": "c",
              "src": "https://aravia.ru/skin-test/img/questions/8c.jpg?v=1",
              "text": "Морщины вокруг глаз"
            },
            {
              "value": "d",
              "src": "https://aravia.ru/skin-test/img/questions/8d.jpg?v=1",
              "text": "Ничего из вышеперечисленного"
            }
          ]
        },
        {
          "title": "9. ПОЖАЛУЙСТА, ПОСМОТРИТЕ В ЗЕРКАЛО ЕЩЕ РАЗ. УСТРАИВАЕТ ЛИ ВАС В ЦЕЛОМ ВНЕШНИЙ ВИД: ТОН И РЕЛЬЕФ КОЖИ?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/9a.jpg?v=1",
              "text": "Меня все устраивает. Тон кожи — ровный, серьезных проблем нет"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/9b.jpg?v=1",
              "text": "Кожа лица выглядит уставшей и тусклой"
            },
            {
              "value": "c",
              "src": "https://aravia.ru/skin-test/img/questions/9c.jpg?v=1",
              "text": "На коже видны покраснения и мелкие сосуды"
            },
            {
              "value": "d",
              "src": "https://aravia.ru/skin-test/img/questions/9d.jpg?v=1",
              "text": "Часто сталкиваюсь с шелушениями и раздражением"
            }
          ]
        },
        {
          "title": "10. Есть ли у вас проявления купероза,  «сосудистые звездочки»?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/10a.jpg?v=1",
              "text": "Да"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/10b.jpg?v=1",
              "text": "Нет"
            }
          ]
        },
        {
          "title": "11. Пользуетесь ли вы декоративной косметикой?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/11a.jpg?v=1",
              "text": "Да"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/11b.jpg?v=1",
              "text": "Нет, либо очень редко"
            }
          ]
        },
        {
          "title": "12. К какому фототипу вы бы себя отнесли?",
          "images": [
            {
              "value": "a",
              "src": "https://aravia.ru/skin-test/img/questions/12a.jpg?v=1",
              "text": "К светлому фототипу"
            },
            {
              "value": "b",
              "src": "https://aravia.ru/skin-test/img/questions/12b.jpg?v=1",
              "text": "К смуглому фототипу"
            }
          ]
        }
      ]


    };
  },
  computed: {

    currentQuestion() {
      return this.questions[this.currentQuestionIndex];
    },
    formatSelectedAnswers() {
      // Format selected answers as "question1 b question2 c"
      return Object.keys(this.selectedAnswers)
          .map((question) => `${question} ${this.selectedAnswers[question]}`)
          .join(" ");
    },

  },
  methods: {
    selectAnswer(value) {
      // Handle the selected answer, store it in selectedAnswers
      this.selectedAnswers[this.currentQuestionIndex] = value;

      // Move to the next question
      this.currentQuestionIndex++;

      // Check if there are more questions
      if (this.currentQuestionIndex >= this.questions.length) {
        console.log("No more questions");
        this.getResult()
        // Perform any action when there are no more questions
      }
    },
    sendAnswers() {
      // Преобразовываем объект selectedAnswers в строку параметров
      const queryParams = Object.entries(this.selectedAnswers)
          .map(([key, value]) => `answers[${encodeURIComponent(key)}]=${encodeURIComponent(value)}`)
          .join('&');

      // Формируем URL для отправки запроса
      const apiUrl = `https://aravia.ru/api.php?method=getSkinTestResult&${queryParams}`;

      // Отправляем GET-запрос по сформированному URL

      axios.get(apiUrl)
          .then(response => {
            // Обработка успешного ответа
            console.log(response.data);
            this.serverResponse = response.data; // Сохраняем ответ сервера
            const $ = cheerio.load(response.data);

            // Находим и извлекаем нужный текст
            const parsedText = $('.your-selector-for-text').text();

            // Отображаем текст на сайте
            console.log('Parsed Text:', parsedText);
          })
          .catch(error => {
            // Обработка ошибки
            console.error('Ошибка при отправке данных:', error);
          });
    },
    getResult() {
      console.log('getResult');
      document.body.classList.add('loading');

      const queryParams = Object.entries(this.selectedAnswers)
          .map(([key, value]) => `answers[${encodeURIComponent(key)}]=${encodeURIComponent(value)}`)
          .join('&');

      const apiUrl = `https://aravia.ru/api.php?method=getSkinTestResult&${queryParams}`;

      // Используем режим 'no-cors' для обхода CORS
      fetch(apiUrl, { method: 'GET', mode: 'cors' })
          .then(response => {
            // В режиме 'no-cors' response будет неполным, но мы можем проверить, был ли запрос успешным
            if (response.ok) {
              return response.text();
            } else {
              throw new Error('Request failed');
            }
          })
          .then(response => {
            // Пример манипуляций с DOM
            const parser = new DOMParser();
            const doc = parser.parseFromString(response, 'text/html');
            const skinTestElement = doc.querySelector('.skin-test');

            // Проверяем, что элемент был найден, прежде чем выполнять операции с ним
            if (skinTestElement) {
              // Удаление класса 'active' из '.skin-test' и добавление 'active' к '.skin-test_result'
              skinTestElement.classList.remove('active');

              // Продолжаем с остальными операциями, только если элемент был найден
              const skinTestResultElement = doc.querySelector('.skin-test_result');
              if (skinTestResultElement) {
                skinTestResultElement.classList.add('active');
                skinTestResultElement.prepend(response);
              }
            }

            // Удаление класса 'loading' из 'body'
            document.body.classList.remove('loading');

            // Вызов цели для Яндекс.Метрики
            ym(46392150, 'reachGoal', 'skin-test-finish');
          })
          .catch(error => {
            // Обработка ошибок
            console.error('Error fetching skin test result:', error);
          });
    }


  },
  mounted() {
    // Fetch questions if needed
    // this.$store.dispatch('fetchQuestions', localStorage.getItem('token'));
  },
};
</script>
