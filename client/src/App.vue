<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        ToDo App
      </div>
    </v-app-bar>
    <v-main>
      <Container />
    </v-main>
  </v-app>
</template>

<script>
import Container from './components/Container';

export default {
  name: 'App',

  components: {
    Container,
  },

  data: () => ({
    //
  }),
};
</script>
