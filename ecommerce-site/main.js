// Fetch products from backend
fetch('/api/products')
    .then(response => response.json())
    .then(data => {
        const products = data.products;
        const productsDiv = document.getElementById('products');
        products.forEach(product => {
            productsDiv.innerHTML += `
                <div class="card">
                    <img src="${product.image}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">${product.name}</h5>
                        <p class="card-text">${product.description}</p>
                        <p class="card-text">$${product.price}</p>
                        <a href="#" class="btn btn-primary">Add to Cart</a>
                    </div>
                </div>
            `;
        });
    });

// Example Stripe Checkout integration
function checkout(amount) {
    var stripe = Stripe('<your_stripe_publishable_key>');
    stripe.redirectToCheckout({
        sessionId: '<your_stripe_session_id>'
    }).then(function (result) {
        if (result.error) {
            console.error(result.error.message);
        }
    });
}
