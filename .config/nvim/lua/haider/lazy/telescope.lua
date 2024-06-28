return {
    'nvim-telescope/telescope.nvim', tag = '0.1.8',
    dependencies = { 'nvim-lua/plenary.nvim' },
    config = function()
        local builtin = require('telescope.builtin')
        vim.keymap.set("n", "<leader>h", builtin.find_files, {})
        vim.keymap.set("n", "<leader>g", builtin.find_files, {})
        vim.keymap.set("n", "<leader>l", function()
			builtin.grep_string({ search = vim.fn.input("Grep > ") })
		end)
    end
}