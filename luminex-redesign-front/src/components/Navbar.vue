<template>

  <section class="top-header">
    <div class="container">
      <div class="row">
        <div class="col-md-4 col-xs-12 col-sm-4">
          <div class="contact-number">
            <a href="tel: 89996442072" ><i class="tf-ion-ios-telephone"></i>8-999-644-20-72</a>
          </div>
        </div>
        <div class="col-md-4 col-xs-12 col-sm-4">
          <!-- Site Logo -->
          <div class="logo text-center">
            <a @click="$router.push({ name: 'Home' });">
              <!-- replace logo here -->
              <svg width="170" height="32" viewBox="0 0 170 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M0.53 31V29.022L4.348 28.24V3.952L0.53 3.17V1.192H21.782V8.736H19.482L18.516 3.722H12.812L8.304 3.998V15.452H15.986L16.63 12.692H18.562V20.604H16.63L15.986 17.89H8.304V28.102L13.548 28.746V31H0.53ZM28.9623 31.322C27.3983 31.322 26.141 31.0613 25.1903 30.54C24.2703 30.0187 23.5956 29.3287 23.1663 28.47C22.7676 27.5807 22.5683 26.63 22.5683 25.618C22.5683 24.33 22.8596 23.2107 23.4423 22.26C24.0556 21.3093 24.9756 20.5273 26.2023 19.914C27.429 19.3007 28.9623 18.8867 30.8023 18.672L34.9423 18.074V14.624C34.9423 13.7347 34.7583 12.9987 34.3903 12.416C34.053 11.8333 33.547 11.4193 32.8723 11.174C32.2283 10.898 31.4156 10.76 30.4343 10.76C29.6676 10.76 29.0236 10.8213 28.5023 10.944C27.981 11.036 27.6743 11.0973 27.5823 11.128L26.8923 15.36C26.8616 15.3907 26.739 15.452 26.5243 15.544C26.3096 15.636 25.9416 15.682 25.4203 15.682C24.899 15.682 24.4083 15.498 23.9483 15.13C23.519 14.7313 23.3043 14.21 23.3043 13.566C23.3043 12.6153 23.657 11.772 24.3623 11.036C25.0983 10.3 25.9876 9.702 27.0303 9.242C28.073 8.75133 29.1156 8.39867 30.1583 8.184C31.201 7.93867 32.0443 7.816 32.6883 7.816C34.007 7.816 35.111 8.06133 36.0003 8.552C36.8896 9.012 37.5643 9.64067 38.0243 10.438C38.4843 11.2353 38.7143 12.1247 38.7143 13.106V27.872L41.9803 28.516V30.264C41.8883 30.2947 41.643 30.3867 41.2443 30.54C40.8763 30.6933 40.3703 30.8467 39.7263 31C39.113 31.1227 38.3923 31.184 37.5643 31.184C36.7056 31.184 36.1076 30.954 35.7703 30.494C35.4636 30.034 35.2796 29.5587 35.2183 29.068H35.0343C34.5743 29.436 34.0223 29.7887 33.3783 30.126C32.765 30.4633 32.0903 30.7547 31.3543 31C30.6183 31.2147 29.821 31.322 28.9623 31.322ZM30.8023 28.424C31.9676 28.424 32.949 28.286 33.7463 28.01C34.5436 27.7033 34.9423 27.55 34.9423 27.55V20.282C33.041 20.4047 31.477 20.65 30.2503 21.018C29.0236 21.386 28.1036 21.892 27.4903 22.536C26.9076 23.1493 26.6163 23.9467 26.6163 24.928C26.6163 27.2587 28.0116 28.424 30.8023 28.424ZM53.9159 31.414C52.0145 31.414 50.3125 31 48.8099 30.172C47.3379 29.344 46.1725 28.102 45.3139 26.446C44.4859 24.79 44.0719 22.72 44.0719 20.236C44.0719 18.6107 44.2865 17.0467 44.7159 15.544C45.1759 14.0413 45.8352 12.7073 46.6939 11.542C47.5832 10.3767 48.6719 9.472 49.9599 8.828C51.2785 8.15333 52.7812 7.816 54.4679 7.816C56.0012 7.816 57.2892 8.092 58.3319 8.644C59.3745 9.16533 60.1565 9.87067 60.6779 10.76C61.2299 11.6187 61.5059 12.554 61.5059 13.566C61.5059 13.934 61.4139 14.2867 61.2299 14.624C61.0459 14.9613 60.7852 15.222 60.4479 15.406C60.1105 15.59 59.6965 15.682 59.2059 15.682C58.8685 15.682 58.5772 15.6513 58.3319 15.59C58.1172 15.498 57.9639 15.4213 57.8719 15.36L57.1819 11.082C57.0592 10.99 56.7219 10.8673 56.1699 10.714C55.6485 10.5607 55.0045 10.484 54.2379 10.484C52.6739 10.484 51.4472 10.8213 50.5579 11.496C49.6992 12.14 49.0859 13.1367 48.7179 14.486C48.3805 15.8353 48.2119 17.568 48.2119 19.684C48.2119 21.7693 48.4725 23.4407 48.9939 24.698C49.5459 25.9247 50.3739 26.814 51.4779 27.366C52.5819 27.918 53.9465 28.194 55.5719 28.194C57.0132 28.194 58.1785 28.056 59.0679 27.78C59.9879 27.504 60.5245 27.32 60.6779 27.228L61.2759 28.608C61.1839 28.7 60.8465 28.976 60.2639 29.436C59.7119 29.896 58.8992 30.3407 57.8259 30.77C56.7832 31.1993 55.4799 31.414 53.9159 31.414ZM74.2227 31.414C71.9534 31.414 70.0827 30.9387 68.6107 29.988C67.1387 29.0067 66.0501 27.6727 65.3447 25.986C64.6394 24.2993 64.2867 22.398 64.2867 20.282C64.2867 17.7673 64.7161 15.5747 65.5747 13.704C66.4641 11.8333 67.6754 10.392 69.2087 9.38C70.7727 8.33733 72.5667 7.816 74.5907 7.816C75.9401 7.816 77.0901 8.046 78.0407 8.506C78.9914 8.966 79.7581 9.59467 80.3407 10.392C80.9541 11.1893 81.3987 12.094 81.6747 13.106C81.9814 14.0873 82.1347 15.1147 82.1347 16.188C82.1347 17.844 81.9814 18.948 81.6747 19.5C81.3681 20.0213 80.7854 20.282 79.9267 20.282H68.3807C68.3807 21.7233 68.6107 23.042 69.0707 24.238C69.5307 25.434 70.2821 26.4 71.3247 27.136C72.3981 27.8413 73.8241 28.194 75.6027 28.194C77.2894 28.194 78.5927 28.0253 79.5127 27.688C80.4634 27.3507 81.0001 27.1513 81.1227 27.09L81.7667 28.378C81.6747 28.47 81.3067 28.7613 80.6627 29.252C80.0494 29.7427 79.1907 30.2333 78.0867 30.724C77.0134 31.184 75.7254 31.414 74.2227 31.414ZM68.4267 18.166L78.2707 17.798C78.3627 17.246 78.4087 16.6327 78.4087 15.958C78.4087 14.21 78.1021 12.8607 77.4887 11.91C76.8754 10.9593 75.6947 10.484 73.9467 10.484C72.6894 10.484 71.6467 10.7907 70.8187 11.404C70.0214 11.9867 69.4234 12.8607 69.0247 14.026C68.6567 15.1607 68.4574 16.5407 68.4267 18.166ZM99.5766 31.506C94.946 31.506 91.5266 30.218 89.3186 27.642C87.1106 25.066 86.0066 21.34 86.0066 16.464C86.0066 14.3787 86.3286 12.3853 86.9726 10.484C87.6473 8.58267 88.6133 6.896 89.8706 5.424C91.128 3.952 92.6613 2.78667 94.4706 1.928C96.28 1.06933 98.3346 0.639999 100.635 0.639999C102.321 0.639999 103.931 0.762666 105.465 1.008C107.029 1.22267 108.332 1.54466 109.375 1.974V9.196H107.075L106.109 4.136C105.373 3.92133 104.453 3.75267 103.349 3.63C102.275 3.47667 101.202 3.4 100.129 3.4C98.0126 3.4 96.2493 3.89067 94.8386 4.872C93.428 5.82267 92.37 7.264 91.6646 9.196C90.9593 11.128 90.6066 13.566 90.6066 16.51C90.6066 18.626 90.8213 20.466 91.2506 22.03C91.68 23.594 92.2933 24.8973 93.0906 25.94C93.888 26.952 94.8693 27.7033 96.0346 28.194C97.2306 28.6847 98.5953 28.93 100.129 28.93C101.355 28.93 102.383 28.838 103.211 28.654C104.069 28.4393 104.744 28.194 105.235 27.918C105.756 27.642 106.139 27.4273 106.385 27.274L107.305 22.536H109.559V29.528C108.976 29.7733 108.255 30.0647 107.397 30.402C106.538 30.7087 105.48 30.9693 104.223 31.184C102.965 31.3987 101.417 31.506 99.5766 31.506ZM120.244 31.322C118.68 31.322 117.422 31.0613 116.472 30.54C115.552 30.0187 114.877 29.3287 114.448 28.47C114.049 27.5807 113.85 26.63 113.85 25.618C113.85 24.33 114.141 23.2107 114.724 22.26C115.337 21.3093 116.257 20.5273 117.484 19.914C118.71 19.3007 120.244 18.8867 122.084 18.672L126.224 18.074V14.624C126.224 13.7347 126.04 12.9987 125.672 12.416C125.334 11.8333 124.828 11.4193 124.154 11.174C123.51 10.898 122.697 10.76 121.716 10.76C120.949 10.76 120.305 10.8213 119.784 10.944C119.262 11.036 118.956 11.0973 118.864 11.128L118.174 15.36C118.143 15.3907 118.02 15.452 117.806 15.544C117.591 15.636 117.223 15.682 116.702 15.682C116.18 15.682 115.69 15.498 115.23 15.13C114.8 14.7313 114.586 14.21 114.586 13.566C114.586 12.6153 114.938 11.772 115.644 11.036C116.38 10.3 117.269 9.702 118.312 9.242C119.354 8.75133 120.397 8.39867 121.44 8.184C122.482 7.93867 123.326 7.816 123.97 7.816C125.288 7.816 126.392 8.06133 127.282 8.552C128.171 9.012 128.846 9.64067 129.306 10.438C129.766 11.2353 129.996 12.1247 129.996 13.106V27.872L133.262 28.516V30.264C133.17 30.2947 132.924 30.3867 132.526 30.54C132.158 30.6933 131.652 30.8467 131.008 31C130.394 31.1227 129.674 31.184 128.846 31.184C127.987 31.184 127.389 30.954 127.052 30.494C126.745 30.034 126.561 29.5587 126.5 29.068H126.316C125.856 29.436 125.304 29.7887 124.66 30.126C124.046 30.4633 123.372 30.7547 122.636 31C121.9 31.2147 121.102 31.322 120.244 31.322ZM122.084 28.424C123.249 28.424 124.23 28.286 125.028 28.01C125.825 27.7033 126.224 27.55 126.224 27.55V20.282C124.322 20.4047 122.758 20.65 121.532 21.018C120.305 21.386 119.385 21.892 118.772 22.536C118.189 23.1493 117.898 23.9467 117.898 24.928C117.898 27.2587 119.293 28.424 122.084 28.424ZM135.859 31V29.114L138.987 28.47V11.864L135.399 11.22V9.334L142.023 8.046L142.805 10.622C142.958 10.4687 143.311 10.1773 143.863 9.748C144.446 9.288 145.105 8.85867 145.841 8.46C146.608 8.03067 147.313 7.816 147.957 7.816C148.601 7.816 149.092 8.03067 149.429 8.46C149.797 8.85867 149.981 9.39533 149.981 10.07C149.981 10.5913 149.858 11.0513 149.613 11.45C149.398 11.8487 149.061 12.2013 148.601 12.508L146.669 12.002C146.301 11.91 145.979 11.8487 145.703 11.818C145.427 11.7567 145.12 11.726 144.783 11.726C144.446 11.726 144.093 11.7567 143.725 11.818C143.357 11.8793 143.035 11.9713 142.759 12.094V28.424L146.991 29.022V31H135.859ZM161.686 31.414C159.416 31.414 157.546 30.9387 156.074 29.988C154.602 29.0067 153.513 27.6727 152.808 25.986C152.102 24.2993 151.75 22.398 151.75 20.282C151.75 17.7673 152.179 15.5747 153.038 13.704C153.927 11.8333 155.138 10.392 156.672 9.38C158.236 8.33733 160.03 7.816 162.054 7.816C163.403 7.816 164.553 8.046 165.504 8.506C166.454 8.966 167.221 9.59467 167.804 10.392C168.417 11.1893 168.862 12.094 169.138 13.106C169.444 14.0873 169.598 15.1147 169.598 16.188C169.598 17.844 169.444 18.948 169.138 19.5C168.831 20.0213 168.248 20.282 167.39 20.282H155.844C155.844 21.7233 156.074 23.042 156.534 24.238C156.994 25.434 157.745 26.4 158.788 27.136C159.861 27.8413 161.287 28.194 163.066 28.194C164.752 28.194 166.056 28.0253 166.976 27.688C167.926 27.3507 168.463 27.1513 168.586 27.09L169.23 28.378C169.138 28.47 168.77 28.7613 168.126 29.252C167.512 29.7427 166.654 30.2333 165.55 30.724C164.476 31.184 163.188 31.414 161.686 31.414ZM155.89 18.166L165.734 17.798C165.826 17.246 165.872 16.6327 165.872 15.958C165.872 14.21 165.565 12.8607 164.952 11.91C164.338 10.9593 163.158 10.484 161.41 10.484C160.152 10.484 159.11 10.7907 158.282 11.404C157.484 11.9867 156.886 12.8607 156.488 14.026C156.12 15.1607 155.92 16.5407 155.89 18.166Z" fill="black"/>
              </svg>

            </a>
          </div>
        </div>
        <div class="col-md-4 col-xs-12 col-sm-4">
          <!-- Cart -->
          <ul class="navbar navbar-expand-lg w-100 justify-content-around">
            <li class="nav-item dropdown cart-nav dropdown-slide">
              <a @click="$router.push({name:'Cart'})" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" style="  text-decoration: none; color: inherit;  background-color: transparent;"><i
                  class="tf-ion-android-cart"></i>Корзина</a>
              <div class="dropdown-menu cart-dropdown">
                <!-- Cart Item -->


                <div class="media">
                  <a class="pull-left" href="#!">
                    <img class="media-object" src="src/static/images/shop/cart/cart-1.jpg" alt="image" />
                  </a>
                  <div class="media-body">
                    <h4 class="media-heading"><a href="#!">Ladies Bag</a></h4>
                    <div class="cart-price">
                      <span>1 x</span>
                      <span>1250.00</span>
                    </div>
                    <h5><strong>$1200</strong></h5>
                  </div>
                  <a href="#!" class="remove"><i class="tf-ion-close"></i></a>
                </div><!-- / Cart Item -->
                <!-- Cart Item -->


                <div class="media">
                  <a class="pull-left" href="#!">
                    <img class="media-object" src="images/shop/cart/cart-2.jpg" alt="image" />
                  </a>
                  <div class="media-body">
                    <h4 class="media-heading"><a href="#!">Ladies Bag</a></h4>
                    <div class="cart-price">
                      <span>1 x</span>
                      <span>1250.00</span>
                    </div>
                    <h5><strong>$1200</strong></h5>
                  </div>
                  <a href="#!" class="remove"><i class="tf-ion-close"></i></a>
                </div><!-- / Cart Item -->

                <div class="cart-summary">
                  <span>Total</span>
                  <span class="total-price">$1799.00</span>
                </div>
                <ul class="text-center cart-buttons">
                  <li><a @click="$router.push({name:'Cart'})" class="btn btn-small">View Cart</a></li>
                  <li><a href="checkout.html" class="btn btn-small btn-solid-border">Checkout</a></li>
                </ul>
              </div>

            </li><!-- / Cart -->

            <!-- Search -->
            <li class="nav-item dropdown search dropdown-slide">
              <a href="#!" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" style="  text-decoration: none; color: inherit;  background-color: transparent;"><i
                  class="tf-ion-ios-search-strong"></i>Поиск</a>
              <ul class="dropdown-menu search-dropdown">
                <li>
                  <form action="post"><input type="search" class="form-control" placeholder="Ваш запрос..."></form>
                </li>
              </ul>
            </li><!-- / Search -->

            <!-- Languages -->
            <li class="commonSelect nav-item">
              <select class="form-control">
                <option>EN</option>
                <option>RU</option>
                <option>DE</option>
                <option>FR</option>
                <option>ES</option>
              </select>
            </li><!-- / Languages -->

          </ul><!-- / .nav .navbar-nav .navbar-right -->
        </div>
      </div>
    </div>
  </section>
  <section class="menu">
    <nav class="navbar navigation">
      <div class="container">
          <a class="navbar-brand" href="#">Дом</a>
          <a class="navbar-brand" href="#">Магазин</a>
          <a class="navbar-brand" href="#">Страницы</a>
          <a class="navbar-brand" href="#">Элементы</a>
          <a class="navbar-brand" href="#">Блог</a>


        <!-- Navbar Links -->
        <div id="navbar" class="navbar-collapse collapse text-center">
          <ul class="nav navbar-nav">

            <!-- Home -->
            <li class="dropdown ">
              <a href="index.html">Home</a>
            </li><!-- / Home -->


            <!-- Elements -->
            <li class="dropdown dropdown-slide">
              <a href="#!" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" data-delay="350"
                 role="button" aria-haspopup="true" aria-expanded="false">Shop <span
                  class="tf-ion-ios-arrow-down"></span></a>
              <div class="dropdown-menu">
                <div class="row">

                  <!-- Basic -->
                  <div class="col-lg-6 col-md-6 mb-sm-3">
                    <ul>
                      <li class="dropdown-header">Pages</li>
                      <li role="separator" class="divider"></li>
                      <li><a href="shop.html">Shop</a></li>
                      <li><a href="checkout.html">Checkout</a></li>
                      <li><a href="cart.html">Cart</a></li>
                      <li><a href="pricing.html">Pricing</a></li>
                      <li><a href="confirmation.html">Confirmation</a></li>

                    </ul>
                  </div>

                  <!-- Layout -->
                  <div class="col-lg-6 col-md-6 mb-sm-3">
                    <ul>
                      <li class="dropdown-header">Layout</li>
                      <li role="separator" class="divider"></li>
                      <li><a href="product-single.html">Product Details</a></li>
                      <li><a href="shop-sidebar.html">Shop With Sidebar</a></li>

                    </ul>
                  </div>

                </div><!-- / .row -->
              </div><!-- / .dropdown-menu -->
            </li><!-- / Elements -->


            <!-- Pages -->
            <li class="dropdown full-width dropdown-slide">
              <a href="#!" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" data-delay="350"
                 role="button" aria-haspopup="true" aria-expanded="false">Pages <span
                  class="tf-ion-ios-arrow-down"></span></a>
              <div class="dropdown-menu">
                <div class="row">

                  <!-- Introduction -->
                  <div class="col-sm-3 col-xs-12">
                    <ul>
                      <li class="dropdown-header">Introduction</li>
                      <li role="separator" class="divider"></li>
                      <li><a href="contact.html">Contact Us</a></li>
                      <li><a href="about.html">About Us</a></li>
                      <li><a href="404.html">404 Page</a></li>
                      <li><a href="coming-soon.html">Coming Soon</a></li>
                      <li><a href="faq.html">FAQ</a></li>
                    </ul>
                  </div>

                  <!-- Contact -->
                  <div class="col-sm-3 col-xs-12">
                    <ul>
                      <li class="dropdown-header">Dashboard</li>
                      <li role="separator" class="divider"></li>
                      <li><a href="dashboard.html">User Interface</a></li>
                      <li><a href="order.html">Orders</a></li>
                      <li><a href="address.html">Address</a></li>
                      <li><a href="profile-details.html">Profile Details</a></li>
                    </ul>
                  </div>

                  <!-- Utility -->
                  <div class="col-sm-3 col-xs-12">
                    <ul>
                      <li class="dropdown-header">Utility</li>
                      <li role="separator" class="divider"></li>
                      <li><a href="login.html">Login Page</a></li>
                      <li><a href="signin.html">Signin Page</a></li>
                      <li><a href="forget-password.html">Forget Password</a></li>
                    </ul>
                  </div>

                  <!-- Mega Menu -->
                  <div class="col-sm-3 col-xs-12">
                    <a href="shop.html">
                      <img class="img-responsive" src="images/shop/header-img.jpg" alt="menu image" />
                    </a>
                  </div>
                </div><!-- / .row -->
              </div><!-- / .dropdown-menu -->
            </li><!-- / Pages -->



            <!-- Blog -->
            <li class="dropdown dropdown-slide">
              <a href="#!" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" data-delay="350"
                 role="button" aria-haspopup="true" aria-expanded="false">Blog <span
                  class="tf-ion-ios-arrow-down"></span></a>
              <ul class="dropdown-menu">
                <li><a href="blog-left-sidebar.html">Blog Left Sidebar</a></li>
                <li><a href="blog-right-sidebar.html">Blog Right Sidebar</a></li>
                <li><a href="blog-full-width.html">Blog Full Width</a></li>
                <li><a href="blog-grid.html">Blog 2 Columns</a></li>
                <li><a href="blog-single.html">Blog Single</a></li>
              </ul>
            </li><!-- / Blog -->

            <!-- Shop -->
            <li class="dropdown dropdown-slide">
              <a href="#!" class="dropdown-toggle" data-toggle="dropdown" data-hover="dropdown" data-delay="350"
                 role="button" aria-haspopup="true" aria-expanded="false">Elements <span
                  class="tf-ion-ios-arrow-down"></span></a>
              <ul class="dropdown-menu">
                <li><a href="typography.html">Typography</a></li>
                <li><a href="buttons.html">Buttons</a></li>
                <li><a href="alerts.html">Alerts</a></li>
              </ul>
            </li><!-- / Blog -->
          </ul><!-- / .nav .navbar-nav -->

        </div>
        <!--/.navbar-collapse -->
      </div><!-- / .container -->
    </nav>
  </section>

</template>

<script>
import Home from "@/views/Home.vue";

export default {

  name: 'NavBar',
  computed: {
    Home() {
      return Home
    }
  }
}
</script>

<style scoped>
.dropdown-toggle::after {
  display: none; /* Скрывает стрелочку вниз */
}
</style>