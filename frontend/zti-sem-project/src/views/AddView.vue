<template>
    <AddPeopleForm :person="{}" @done="backToPeople">
        <template v-slot:title>
            <h1>
                Add New Person
            </h1>
        </template>
    </AddPeopleForm>
</template>

<script>
import AddPeopleForm from '../components/AddPeopleForm.vue'

export default {
    components:
    {
        AddPeopleForm
    },
    methods: {
        backToPeople()
        {
            this.$router.push("/people")
        }
    },
}
</script>

<style>

</style>