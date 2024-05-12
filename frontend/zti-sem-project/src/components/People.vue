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
                    <button @click="handleEdit(person)">
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
            <PeopleModal :person="chosen" :edit="edit" @close="showModal" @edit="showEdit" @reload="loadPeople"/>
        </teleport>
    </div>
</template>

<script>
import PeopleModal from "@/components/PeopleModal.vue"
import AddPeopleForm from '@/components/AddPeopleForm.vue'
const BASE_URL = "http://localhost:3000"

export default {
    data(){
        return{
            loading: true,
            show: false,
            edit: false,
            people: [],
            chosen: {},
        }
    },
    components:{
        PeopleModal,
        AddPeopleForm
    },
    mounted(){
        this.loadPeople()
    },
    methods: {
        async loadPeople()
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
        handleEdit(person)
        {
            this.showEdit(person)
        },
        async handleDelete(person)
        {
            const uri = "?fname=" + encodeURIComponent(person.fname)
                        + "&lname=" + encodeURIComponent(person.lname)

            await fetch(BASE_URL + "/person" + uri, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                }
                })
            .catch((err) => console.log(err.message))

            await this.loadPeople()
        },
        async showEdit(person){
            this.chosen = person
            this.edit = !this.edit
            this.show = !this.show
            await this.loadPeople()
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

    .person {
        margin: auto;
        max-width: 450px;
        margin-bottom: 15px;
        padding: 10px;
        border-radius: 5px;
        background: #f2f2f2;
    }
</style>