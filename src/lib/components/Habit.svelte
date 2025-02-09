<script lang="ts">
  import { Check, Dumbbell } from "lucide-svelte"
</script>

<div class="grid gap-2 p-2 rounded border border-gray-200 dark:border-gray-800">
  <div class="flex items-stretch justify-between">
    <div class="flex items-stretch gap-2">
      <div
        class="flex aspect-square items-center justify-center bg-gray-200 dark:bg-gray-800 rounded"
      >
        <Dumbbell class="h-4 w-4" />
      </div>
      <div>
        <p class="truncate text-sm">Gym</p>
        <p class="truncate text-xs">Lift heavy things.</p>
      </div>
    </div>
    <button
      class="flex aspect-square items-center justify-center bg-gray-200 dark:bg-gray-800 rounded"
    >
      <Check class="h-4 w-4" />
    </button>
  </div>
  <div class="grid grid-cols-35 gap-0.5">
    {#each { length: 35 * 7 }, index}
      <div
        class="aspect-square w-full rounded-xs bg-gray-200 dark:bg-gray-800"
      ></div>
    {/each}
  </div>
</div>
