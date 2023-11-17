<template>

  <body>
  <section class="page-header">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="content">
            <h1 class="page-name">С возвращением!</h1>
            <p>Мы рады видеть вас снова!</p>
          </div>
        </div>
      </div>
    </div>
  </section>

    <div class="checkout shopping">
      <div class="container">
        <div class="row">
          <div class="col align-self-center">
            <div class="block billing-details">
              <form class="checkout-form">
                <div class="form-group">
                  <p>Адрес электронной почты или номер телефона</p>
                  <input v-model="email" type="text" class="form-control" id="emailOrPhone" placeholder="">
                </div>
                <div class="form-group">
                  <p>Фамилия Имя</p>
                  <input v-model="name" type="text" class="form-control " id="emailOrPhone" placeholder="">
                </div>
                <div class="form-group">
                  <p>День рождения</p>
                  <div class="row">
                    <div class="col">
                      <p for="day">День:</p>
                      <input class="form-control" type="number" id="day" name="day" min="1" max="31" v-model="birthday.day" required>
                    </div>
                    <div class="col">
                      <p for="month">Месяц:</p>
                      <select class="form-control" id="month" name="month" v-model="birthday.month" required>
                        <option value="1">Январь</option>
                        <option value="2">Февраль</option>
                        <option value="3">Март</option>
                        <option value="4">Апрель</option>
                        <option value="5">Май</option>
                        <option value="6">Июнь</option>
                        <option value="7">Июль</option>
                        <option value="8">Август</option>
                        <option value="9">Сентябрь</option>
                        <option value="10">Октябрь</option>
                        <option value="11">Ноябрь</option>
                        <option value="12">Декабрь</option>
                      </select>
                    </div>
                    <div class="col">
                      <p for="year">Год:</p>
                      <input class="form-control" type="number" id="year" name="year" min="1900" max="2023" v-model="birthday.year" required>
                    </div>
                  </div>
                </div>
                <div class="form-group">
                  <p>Пароль</p>
                  <input v-model="password" type="password" class="form-control" id="password" placeholder="">
                </div>
                <div>
                  <button class="btn btn-success btn-lg">Продолжить</button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>

  </body>
</template>

<script>
export default {
  name: "RegisterView",
  data() {
    return {
      firstname: name.split(" ")[0],
      secondname: name.split(" ")[1],
      name: "",
      email: "",
      password: "",
      birthday: {
        day: "",
        month: "",
        year: ""
      }
    };
  },
  computed: {
    firstname() {
      return this.name.split(" ")[0] || "";
    },
    secondname() {
      return this.name.split(" ")[1] || "";
    }
  },
  watch: {
    name(newValue) {
      // Update firstname and secondname when name changes
      this.firstname = newValue.split(" ")[0] || "";
      this.secondname = newValue.split(" ")[1] || "";
    }
  }
}

</script>