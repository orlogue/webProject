<template>
  <div id="app">
    <HelloWorld/>
    {{ profiles }}
<!--    sjglskdjglksdjgs-->
<!--    <ul>-->
<!--      <li v-for="(profile, index) in object.data['profiles']" :key="index">{{ profile }}</li>-->
<!--    </ul>-->
<!--    <li v-for="(profile, index) in object.data['profiles']" :key="index">{{ profile }}</li>-->
  </div>
</template>

<script>
import axios from 'axios'
import HelloWorld from "./components/HelloWorld";

export default {
  name: 'app',
  components: {HelloWorld},
  // data: () => ({
  //   profiles: []
  // }),
  data() {
    return {
      profiles: []
    }
  },
  mounted () {
    axios.get('http://localhost:8000/api/profiles/').then((response) => {
      this.profiles = response.data
    })
  }
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
