<template>
    <header>
        <img alt="Virtualis logo" src="../assets/virtuaulisLogo.png" height="50">
        <h2>Dnevni zadatci</h2>
    <nav>
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </nav>
     </header>
</template>
<style>
header {
    display: flex;
    border-bottom: 1px solid #ccc;
    padding: .5rem 1rem;
    background-color: rgba(0,123,255,0.5); /* Blue navbar */
    color: white;
}

nav {
    margin-left: auto;
    ul {
        list-style: none;
    }

    ul li {
        display: inline flex;
        margin-left: 1rem;
    }
}


</style>
