<template>
  <v-app v-bind:style="{ background: `url(${this.photoUrl})  center / 100%` }">
    <v-main>
      <v-container class="d-flex align-center justify-center fill-height">
        <v-card class="mx-auto" width="500">
          <v-card-text>
            <div>Select Files</div>
          </v-card-text>
          <div>
            <v-col>
              <v-file-input
                prepend-icon="mdi-video"
                placeholder="Select your video"
                truncate-length="15"
              ></v-file-input>
              <v-file-input
                prepend-icon="mdi-text"
                placeholder="Select your subtitle"
                truncate-length="15"
              ></v-file-input>
            </v-col>
          </div>

          <v-card-actions>
            <v-btn text color="teal accent-4" @click="reveal = true">
              Next
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
export default Vue.extend({
  name: 'App',

  components: {},
  mounted() {
    this.$http
      .get(
        'https://api.unsplash.com/photos/random?client_id=iphDzKW79-nCEtPXnOwr-zC7ztSdiGGVcvWo0MQc9Qw',
        {
          headers: {
            // Authorization: 'iphDzKW79-nCEtPXnOwr-zC7ztSdiGGVcvWo0MQc9Qw',
            'Access-Control-Allow-Origin': '*',
          },
        },
      )
      .then((res: any) => {
        this.photoUrl = res.body.urls.full;
        console.log(this.photoUrl);
      });
  },
  data: () => ({
    photoUrl: '123',
  }),
});
</script>

<style scoped></style>
