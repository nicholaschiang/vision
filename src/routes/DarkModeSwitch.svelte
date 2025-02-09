<script lang="ts">
  import { browser } from "$app/environment"

  let darkMode = $state(true)

  function handleSwitchDarkMode() {
    darkMode = !darkMode

    localStorage.setItem("theme", darkMode ? "dark" : "light")

    darkMode
      ? document.documentElement.classList.add("dark")
      : document.documentElement.classList.remove("dark")
  }

  if (browser) {
    if (
      localStorage.theme === "dark" ||
      (!("theme" in localStorage) &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
    ) {
      document.documentElement.classList.add("dark")
      darkMode = true
    } else {
      document.documentElement.classList.remove("dark")
      darkMode = false
    }
  }
</script>

<button
  class="px-0.5 py-1 text-left text-gray-400 hover:text-inherit dark:text-gray-600 transition"
  onclick={handleSwitchDarkMode}>Theme</button
>
