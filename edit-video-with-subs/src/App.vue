<template>
  <v-app v-bind:style="{ background: `url(${this.photoUrl})  center / 100%` }">
    <v-main>
      <v-container class="d-flex align-center justify-center fill-height">
        <v-card class="mx-auto" width="500">
          <v-card-title class="title font-weight-regular justify-space-between">
            <span>{{ currentTitle }}</span>
            <v-avatar
              color="primary lighten-2"
              class="subheading white--text"
              size="24"
              v-text="step"
            ></v-avatar>
          </v-card-title>

          <v-window v-model="step">
            <v-window-item :value="1">
              <v-card-text>
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
                <span class="caption grey--text text--darken-1">
                  Please select a video and srt file which is suit for the video
                </span>
              </v-card-text>
            </v-window-item>

            <v-window-item :value="2">
              <v-card-title>
                Subs
                <v-spacer></v-spacer>
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Search"
                  single-line
                  hide-details
                ></v-text-field>
              </v-card-title>
              <v-data-table
                :headers="headers"
                :items="desserts"
                :search="search"
                show-select
              ></v-data-table>
            </v-window-item>
            <v-window-item :value="3">
              <div class="pa-4 text-center">
                <v-img
                  class="mb-4"
                  contain
                  height="128"
                  src="https://cdn.vuetifyjs.com/images/logos/v.svg"
                ></v-img>
                <h3 class="title font-weight-light mb-2">
                 Preview
                </h3>
                <span class="caption grey--text">Thanks for signing up!</span>
              </div>
            </v-window-item>

            <v-window-item :value="4">
              <div class="pa-4 text-center">
                <v-img
                  class="mb-4"
                  contain
                  height="128"
                  src="https://cdn.vuetifyjs.com/images/logos/v.svg"
                ></v-img>
                <h3 class="title font-weight-light mb-2">
                  Welcome to Vuetify
                </h3>
                <span class="caption grey--text">Thanks for signing up!</span>
              </div>
            </v-window-item>
          </v-window>

          <v-card-actions>
            <v-btn :disabled="step === 1" text @click="step--">
              Back
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
              :disabled="step === 4"
              color="primary"
              depressed
              :loading="loading"
              @click="remove"
            >
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
    // this.$http
    //   .get(
    //     "https://api.unsplash.com/photos/random?client_id=iphDzKW79-nCEtPXnOwr-zC7ztSdiGGVcvWo0MQc9Qw",
    //     {
    //       headers: {
    //         // Authorization: "iphDzKW79-nCEtPXnOwr-zC7ztSdiGGVcvWo0MQc9Qw",
    //         "Access-Control-Allow-Origin": "*",
    //       },
    //     },
    //   )
    //   .then((res: any) => {
    //     this.photoUrl = res.body.urls.full;
    //     console.log(this.photoUrl);
    //   });
  },
  data: () => ({
    photoUrl: '123',
    step: 1,
    panel: [0, 1],
    disabled: false,
    loading: false,
    search: '',
    headers: [
      {
        text: 'Text',
        align: 'start',
        sortable: false,
        value: 'text',
      },
      { text: 'Start-Time', value: 'startTime' },
      { text: 'End-Time', value: 'endTime' },
    ],
    desserts: [
      {
        text: "Yeah, you -- you can stop. I'm  just gonna keep telling them",
        startTime: '00:00:47,221',
        endTime: '00:00:48,265',
      },
    ],
  }),
  methods: {
    async remove() {
      this.loading = true;

      await new Promise(resolve => setTimeout(resolve, 1000));
      this.step++;
      this.loading = false;
    },
  },
  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return 'Select-Files';
        case 2:
          return 'Select-Subs';
        case 3:
          return 'Make-up';
        case 4:
          return 'Generator-Standar-Card';
        default:
          return '';
      }
    },
  },
});
</script>

<style scoped>
.pd {
  padding: 0 16px 16px;
}
</style>
