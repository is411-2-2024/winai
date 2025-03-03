<script>
    let quantity = 0

    function increment() {
        quantity += 1
    }

    function decrement() {
        if (quantity === 0) {
            return
        }

        quantity -= 1
    }
</script>

<span>Current quantity: {quantity}</span>
<div>
    <button class="button" on:click={decrement}>-</button>
    <button class="button" on:click={increment}>+</button>
</div>