(function () {
    const key = 'theme'
    const root = document.documentElement


    function apply(theme) {
        if (theme === 'dark') root.setAttribute('data-theme', 'dark')
        else root.removeAttribute('data-theme')
    }


    const saved = localStorage.getItem(key)
    apply(saved)


    window.addEventListener('DOMContentLoaded', () => {
        const btn = document.getElementById('themeToggle')
        if (!btn) return


        btn.addEventListener('click', () => {
            const isDark = root.getAttribute('data-theme') === 'dark'
            const next = isDark ? 'light' : 'dark'
            if (next === 'dark') localStorage.setItem(key, 'dark')
            else localStorage.removeItem(key)
            apply(next === 'dark' ? 'dark' : 'light')
        })
    })
})()