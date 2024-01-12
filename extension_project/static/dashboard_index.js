const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn")
const themeToggler = document.querySelector(".themeToggler")

// show sidebar
menuBtn.addEventListener('click', () =>{
    sideMenu.style.display = 'block';
})

// close sidebar
closeBtn.addEventListener('click', () =>{
    sideMenu.style.display = 'none';
})

// change theme
themeToggler.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme-variables');

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})


//fill orders in table

Orders.forEach(order => {
    const tr = document.createElement('tr');
    const trContent = `
                        <td>${order.serviceName}</td>
                        <td>${order.amount}</td>
                        <td>${order.dueDate}</td>
                        <td class="${order.paymentStatus === 'Active' ? 'success' :
                        order.shipping === 'Due' ? 'warning' : 'primary'}">${order.paymentStatus}</td>
                        `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);
})


