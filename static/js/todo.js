new Vue ({
	el: '#taskList',
	data: {
		title: 'to do list',
		tasks: [
			{ name: 'Write your first task' },
		]
	},
	methods: {
		newItem: function() {
			if (!this.tasks.name) {
				return
			}
			this.tasks.push ( {
				name: this.tasks.name,
				del: ''
			});
      this.tasks.name = "";
		},
		delItem: function (task) {
			this.tasks.splice(this.tasks.indexOf(task), 1)
		}
	}
})