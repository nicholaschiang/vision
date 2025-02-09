<script lang="ts">
  import { browser } from "$app/environment"

  let darkMode = true

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
  class="px-0.5 py-1 text-left text-gray-600 hover:text-inherit dark:text-gray-400"
  onclick={handleSwitchDarkMode}>Theme</button
>
