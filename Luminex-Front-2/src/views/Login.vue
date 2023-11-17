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
  <div class="page-wrapper">
    <div class="checkout shopping">
      <div class="container">
        <div class="row">
          <div class="col-auto">
            <div class="block billing-details">
              <form class="checkout-form">
                <div class="form-group">
                  <p>Адрес электронной почты или номер телефона</p>
                  <input type="text" class="form-control" id="emailOrPhone" placeholder="">
                </div>
                <div class="form-group">
                  <p>Пароль</p>
                  <input type="password" class="form-control" id="password" placeholder="">
                </div>
                <a href="#">Забыли пароль?</a>
                <div>
                  <button class="btn btn-success btn-lg">Вход</button>
                </div>
                <p>Нужна учетная запись?<a class="text-info" @click="$router.push({ name: 'Register' })"> Зарегистироваться!</a></p>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </body>
</template>

<script>
export default {
  name: "LoginView",
}
</script>