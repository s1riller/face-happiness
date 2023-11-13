<template>
   <navbar></navbar>
  <div class="app">

    <router-view></router-view>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

  </div>
</template>

<script>
import navbar from "@/components/navbar";
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import {mapGetters,mapActions ,mapState,mapMutations} from 'vuex'
import { } from 'vuex'
export default {
  name: "app",
  components: {
    navbar,
  },
  methods:{
    // ...mapActions({load:'loadReactions'})
  },
  created() {
    // this.load(1000)

  }
  ,
 // computed:{
    // ...mapGetters(['getReacions'])
   // ,
   // reactions(){
   //    return this.getReacions
   // }
 // }

}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;

    font-family: "gg sans", sans-serif;

}

</style>
