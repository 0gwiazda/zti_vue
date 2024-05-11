<template>
    <div class="main">
        <div v-if="!loading"> 
            <div v-for="person in people" :key="person" class="person">
                <h3>
                    {{person.fname + ' ' + person.lname}}
                </h3>
                <div class="inputs">
                    <button @click="showModal(person)">
                        Show
                    </button>
                    <button @click="handleEdit">
                        Edit
                    </button>
                    <button @click="handleDelete(person)">
                        Delete
                    </button>
                </div>
            </div>
        </div>
        <div v-else>
            <h2>
                Loading...
            </h2>
        </div>
        <teleport to='.tele' v-if="show">
            <PeopleModal :person="chosen" @close="showModal"/>
        </teleport>
    </div>
</template>

<script>
import PeopleModal from "@/components/PeopleModal.vue"
const BASE_URL = "http://localhost:3000"

export default {
    data(){
        return{
            loading: true,
            show: false,
            people: [],
            chosen: {},
        }
    },
    components:{
        PeopleModal
    },
    mounted(){
        this.loadPeople()
    },
    methods: {
        loadPeople()
        {
            fetch(BASE_URL + "/person")
            .then((res) => res.json())
            .then((data) => {
                this.people = data.people
                this.loading = false
                console.log(this.people)
            })
            .catch((err) => {console.log(err.message)})
        },
        handleEdit()
        {

        },
        handleDelete(person)
        {
            const uri = "?fname=" + encodeURIComponent(person.fname)
                        + "&lname=" + encodeURIComponent(person.lname)

            fetch(BASE_URL + "/person" + uri, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                }
                })
            .catch((err) => console.log(err.message))

            this.loadPeople()
        },
        showModal(person)
        {
            this.chosen = person
            this.show = !this.show
        }
    }
}
</script>

<style>
    button {
        display: inline-block;
        padding: 10px 20px;
        margin: 6px;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s, color 0.3s;
        background-color: #61ce92;
        color: #ffffff;
    }


    button:hover {
        background-color: #54af7d;
    }

    button:active {
    background-color: #388e3c;
    }
</style>