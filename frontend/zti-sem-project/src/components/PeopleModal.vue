<template>
    <div class="backdrop" @click.self="closeModal">
        <div class="modal" v-if="!edit">
            <h1>{{person.fname + ' ' + person.lname}}</h1>
            <h3>
                {{person.city}}
            </h3>
            <h3>
                {{(person.email != null) ? person.email : "No email"}}
            </h3>
            <h3>
                {{(person.tel != null) ? person.tel : "No telephone"}}
            </h3>
        </div>
        <div class="modal" v-else>
            <AddPeopleForm :person="person" @done="closeModal">
                <template v-slot:title>
                    <h1>
                        Edit {{person.fname}}
                    </h1>
                </template>
            </AddPeopleForm>
        </div>
    </div>
</template>

<script>
import AddPeopleForm from '@/components/AddPeopleForm.vue'

export default {
    props: {
        person: {},
        edit: false
    },
    components: {
        AddPeopleForm
    },
    methods: {
        closeModal()
        {
            if(!this.edit){
                this.$emit('close')
            }
            else{
                this.$emit('edit')
                this.$emit('reload')
            }
        }
    }
}
</script>

<style>
    .modal{
        width: 400px;
        padding: 20px;
        margin: 100px auto;
        background: white;
        border-radius: 10px;
        display: flex;
        flex-direction: column;
    }
    .backdrop{
        top: 0;
        position: fixed;
        background: rgba(0,0,0,0.5);
        width: 100%;
        height: 100%;
    }
    .modal h1{
        color: #fa0;
        border: none;
        padding: 0;
    }

    .modal.sale {
        background: crimson;
        color: white;
    }

    .modal.sale h1{
        color: white;
    }
</style>