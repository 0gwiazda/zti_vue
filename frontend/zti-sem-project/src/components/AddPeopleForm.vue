<template>
    <div class="add-form">
        <slot name="title"></slot>
        <form @submit.prevent="onSubmit">
            <label>First Name:</label>
            <input type="text" name="" id="fname" required v-model="newPerson.fname">
            
            <label>Last Name:</label>
            <input type="text" name="" id="lname" required v-model="newPerson.lname">

            <label>City:</label>
            <input type="text" name="" id="city" required v-model="newPerson.city">

            <label>Email:</label>
            <input type="email" name="" id="email" v-model="newPerson.email">

            <label>Telephone:</label>
            <input type="text" name="" id="tel" v-model="newPerson.tel">

            <button type="submit">Send</button>
        </form>
    </div>
</template>

<script>
const BASE_URL = "http://localhost:3000"

export default {
    data()
    {
        return{
            isEdit: false,
            newPerson: {
                fname: "",
                lname: "",
                city: "",
                email: "",
                tel: "",
            }
        }
    },
    props:{
        person: {}
    },
    mounted(){
        this.isEdit = Object.keys(this.person).length !== 0
        if(this.isEdit)
        {
            this.newPerson = JSON.parse(JSON.stringify(this.person))
        }
    },
    methods: {
        onSubmit(){
            if(this.isEdit)
            {
                const uri = "?first_name=" + encodeURIComponent(this.person.fname)
                            + "&last_name=" + encodeURIComponent(this.person.lname)
                console.log(uri)
                console.log(this.newPerson)
                fetch(BASE_URL + "/person/" + uri, {
                    method: "PUT",
                    headers:{
                        "Content-Type":"application/json"
                    },
                    body: JSON.stringify(this.newPerson)
                })
                .catch((err) => console.log(err.message))
            }
            else
            {
                fetch(BASE_URL + "/person", {
                    method: "POST",
                    headers:{
                        "Content-Type":"application/json"
                    },
                    body: JSON.stringify(this.newPerson)
                })
                .catch((err) => console.log(err.message))
            }
            
            this.$emit('done')
        }
    },
}
</script>

<style>
    /* Form Style */
    form {
        max-width: 400px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f2f2f2;
        border-radius: 5px;
    }

    input {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
    }


</style>