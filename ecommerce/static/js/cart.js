var updateBtns = document.getElementsByClassName('update-cart')

for(i=0;i<updateBtns.length;i++)
{
    updateBtns[i].addEventListener('click',function()
    {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId,'Action: ',action)

        console.log(user)

        if (user==='AnonymousUser')
        {
            console.log("NOT LOGGED IN")
        }
        else{
            updateUserOrder(productId,action)
        }
        

    }
    )
}

