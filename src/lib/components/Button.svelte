<script lang="ts">
  let props = $props()
</script>

<button
  {...props}
  class={[
    "rounded border border-gray-200 px-1.5 py-0.5 text-sm text-gray-600 data-active:border-gray-600 data-active:text-gray-950 dark:border-gray-800 dark:text-gray-400 dark:data-active:border-gray-400 dark:data-active:text-gray-50",
    props.class,
  ]}
>
  {@render props.children?.()}
</button>
