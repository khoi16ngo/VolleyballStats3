<template>
    <div>
      <iframe
        width="640"
        height="360"
        :src="youtubeEmbedUrl"
        frameborder="0"
        allowfullscreen
        ref="video"
      ></iframe>
  
      <div class="space-x-2 mt-2">
        <button @click="tagAction('spike')">Spike</button>
        <button @click="tagAction('dig')">Dig</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref } from 'vue'
  
  const youtubeEmbedUrl = 'https://www.youtube.com/embed/YOUR_VIDEO_ID'
  const tagAction = async (type) => {
    const action = {
      time_in_video: getCurrentTime(),
      action_type: type,
      player: 'Khoi', // later make this dynamic
    }
    await axios.post('/api/actions/', action)
  }
  
  const getCurrentTime = () => {
    // This would be tied to YouTube API if you want real time
    return Math.random() * 100 // placeholder
  }
  </script>
  