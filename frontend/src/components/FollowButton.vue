<template>
  <div class="control" id='follow-button'>
    <div class="tags has-addons">
      <span class="tag is-dark">followers</span>
      <span class="tag" :class="getTagClass">{{ count }}</span>
      <a class="tag is-link" :class="getTagClass" @click="fetch_following">Follow</a>
    </div>
  </div>
</template>

<script>
const axios = require('axios');
import { gsap } from "gsap";
export default {
  name: "FollowButton",
  props: {
    target_user_id: String,
    followers_count: String,
    is_followed: Boolean,
  },
  data() {
    return {
      count: this.followers_count,
      followed: this.is_followed
    }
  },
  computed: {
    getTagClass() {
      return this.followed ? "is-success" : "is-info"
    }
  },
  methods: {
    animate_shake() {
    gsap.to('#follow-button', {x:8, clearProps:"x", yoyo: true, repeat:5, duration:0.04});

    },
    animate_blink() {
    gsap.to('#follow-button', {scale: 1.2, clearProps:"scale", duration:0.06})
    },

    fetch_following() {
      axios.get(`/auth_by_email/following/${this.target_user_id}/`)
          .then(response => {
            this.animate_blink();
            this.followed = response.data.is_followed;
            this.count = response.data.count;
          })
      .catch(error => {
        this.animate_shake()
        console.log(error.response.data)
      })
    },
  }
}
</script>

<style scoped>

</style>