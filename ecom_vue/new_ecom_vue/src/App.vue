<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Garas</strong></router-link>


        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navar-menu" @click="showMobileMenu =  !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">summer</router-link>
          <router-link to="/winter" class="navbar-item">winter</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>

              <router-link to="/cart" class="button is-sucess">
                <span class="icon"><i class="fas fa-shopping-cart"></i> </span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view/>
      </section>
      
      <footer class="footer">
        <p class="has-text-centered">Copyright</p>
      </footer>
  
  </div>
</template>
<script>
export default {
  data () {
    return {
      showMobileMenu: false
    };
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
