if (window.lucide) {
    window.lucide.createIcons();
}

document.addEventListener('DOMContentLoaded', () => {
    const dashboardMenuToggle = document.getElementById('dashboardMenuToggle');
    const dashboardSidebar = document.getElementById('sidebar');
    const dashboardSidebarOverlay = document.getElementById('dashboardSidebarOverlay');
    const siteMenuToggle = document.getElementById('siteMenuToggle');
    const siteMobileMenu = document.getElementById('siteMobileMenu');
    const siteMenuClose = document.getElementById('siteMenuClose');

    const closeDashboardMenu = () => {
        if (!dashboardSidebar || !dashboardSidebarOverlay || !dashboardMenuToggle) return;
        dashboardSidebar.classList.remove('is-open');
        dashboardSidebarOverlay.classList.remove('is-visible');
        dashboardMenuToggle.setAttribute('aria-expanded', 'false');
        dashboardMenuToggle.setAttribute('aria-label', 'Open navigation menu');
    };

    if (dashboardMenuToggle && dashboardSidebar && dashboardSidebarOverlay) {
        dashboardMenuToggle.addEventListener('click', () => {
            const isOpen = dashboardSidebar.classList.toggle('is-open');
            dashboardSidebarOverlay.classList.toggle('is-visible', isOpen);
            dashboardMenuToggle.setAttribute('aria-expanded', String(isOpen));
            dashboardMenuToggle.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
        });
        dashboardSidebarOverlay.addEventListener('click', closeDashboardMenu);
        dashboardSidebar.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeDashboardMenu));
    }

    // PUBLIC SITE MOBILE MENU
    const closeSiteMenu = () => {
        if (!siteMenuToggle || !siteMobileMenu) return;
        siteMobileMenu.classList.add('hidden');
        siteMenuToggle.setAttribute('aria-expanded', 'false');
        siteMenuToggle.setAttribute('aria-label', 'Open navigation menu');
    };

    if (siteMenuToggle && siteMobileMenu) {
        siteMenuToggle.addEventListener('click', () => {
            const isOpen = siteMobileMenu.classList.toggle('hidden') === false;
            siteMenuToggle.setAttribute('aria-expanded', String(isOpen));
            siteMenuToggle.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
        });
        siteMobileMenu.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeSiteMenu));
        if (siteMenuClose) siteMenuClose.addEventListener('click', closeSiteMenu);
        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') closeSiteMenu();
        });
    }

    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768) {
            closeDashboardMenu();
            closeSiteMenu();
        }
    });
});

// Add Project modal handling
const addModal = document.getElementById('projectModal');
const addButton = document.getElementById('addButton');
const addClose = document.getElementById('closeModal');
function closeProjectModal(){ addModal.classList.add('hidden'); }
if(addButton){
    addButton.addEventListener('click', () => {
        // reset form fields
        const form = addModal.querySelector('form');
        if(form) form.reset();
        addModal.classList.remove('hidden');
    });
}
if(addClose){ 
    addClose.addEventListener('click', closeProjectModal); 
}
if(addModal){
    addModal.addEventListener('click', function(e){ if(e.target === addModal) closeProjectModal(); 
    });
}
