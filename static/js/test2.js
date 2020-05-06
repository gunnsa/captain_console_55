

function add_to_cart() {
    console.log('hello from add_to_cart()')

    var product = document.getElementsByClassName('product-details')[0]
    console.log('product: ', product)

    console.log('attributes: ', product.attributes)

    var name = product.attributes[1]
    console.log('name: ', name)

    var price = product.attributes[2]
    console.log('price: ', price)

    var id = product.attributes[3]
    console.log('id: ', id)

    //console.log('attributes: ', product)

    //console.log((product.data-name).nodeValue())
    //console.log((product.data-price))

    var price = document.getElementsByTagName('data-price')
    //console.log('price: ', price)
}