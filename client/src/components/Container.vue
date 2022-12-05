<template>
  <v-container>
    <v-data-table
        :headers="headers"
        :items="items"
        sort-by="calories"
        class="elevation-1"
    >
      <template v-slot:top>
        <v-toolbar
            flat
        >
          <v-toolbar-title>Tasks</v-toolbar-title>
          <v-divider
              class="mx-4"
              inset
              vertical
          ></v-divider>
          <v-spacer></v-spacer>
          <v-dialog
              v-model="dialog"
              max-width="500px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                  color="primary"
                  dark
                  class="mb-2"
                  v-bind="attrs"
                  v-on="on"
              >
                Add Task
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">{{ formTitle }}</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col
                        cols="12"
                    >
                      <v-text-field
                          v-model="editedItem.title"
                          label="Title"
                      />
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col
                        cols="12"
                    >
                      <v-text-field
                          v-model="editedItem.body"
                          label="Body"
                      />
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="close"
                >
                  Cancel
                </v-btn>
                <v-btn
                    color="blue darken-1"
                    text
                    @click="dialogMode === 'add' ? createItem() : updateItem()"
                >
                  {{dialogMode === 'add' ? 'Save' : 'Update'}}
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
            <v-card>
              <v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
                <v-spacer></v-spacer>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-toolbar>
      </template>
      <!-- eslint-disable-next-line -->
      <template v-slot:item.actions="{ item }">
        <v-icon
            small
            class="mr-2"
            @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
            small
            @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Container',
  data: () => ({
    items: [],
    dialog: false,
    dialogMode: 'add',
    dialogDelete: false,
    headers: [
      {
        text: 'Title',
        align: 'start',
        sortable: false,
        value: 'title',
      },
      {text: 'Body', value: 'body'},
      {text: 'Actions', value: 'actions', sortable: false},
    ],
    editedItem: {
      title: '',
      body: '',
    },
    defaultItem: {
      title: '',
      body: '',
    },
  }),
  computed: {
    formTitle() {
      if (this.dialogMode === 'add'){
        return 'Add Task'
      }else{
        return 'Edit Task'
      }
    },
  },
  watch: {
    dialog(val) {
      val || this.close()
    },
    dialogDelete(val) {
      val || this.closeDelete()
    },
  },
  created() {
    this.getItems()
  },
  methods: {
    async getItems() {
      this.items = await this.axios.get('http://localhost:8000/tasks').then((res) => res.data)
    },
    editItem(item) {
      this.dialogMode = 'edit'
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    async updateItem(){
      const resp = await this.axios.put(`http://localhost:8000/blogs/${this.editedItem.id}/`, this.editedItem)
          .then((res) => res.data)
      console.log('update resp', resp)
    },
    deleteItem(item) {
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm() {
      this.closeDelete()
    },
    close() {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
      })
    },
    closeDelete() {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
      })
    },
    async createItem() {
      await this.axios.post('http://localhost:8000/tasks/', this.editedItem)
      this.close()
      this.getItems()
    },
  }
}
</script>
