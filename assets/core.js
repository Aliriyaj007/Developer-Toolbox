/* assets/core.js */

/**
 * Developer Toolbox Core Module
 * Handles Theme Switching, Backup/Restore features, and UI interactions
 */

const AppCore = (() => {
  // Constants
  const THEME_KEY = 'tbx_theme';
  const AVAILABLE_THEMES = ['dark', 'light', 'solarized', 'neon', 'highcontrast'];

  // DOM Elements
  const els = {
    themeSelect: null,
    btnBackup: null,
    btnRestore: null,
    restoreInput: null,
    toastContainer: null
  };

  /**
   * Initialize Core Features
   */
  const init = () => {
    // Inject Toast Container
    if(!document.querySelector('.toast-container')) {
      els.toastContainer = document.createElement('div');
      els.toastContainer.className = 'toast-container';
      document.body.appendChild(els.toastContainer);
    } else {
        els.toastContainer = document.querySelector('.toast-container');
    }

    initTheme();
    bindSettingsControls();
  };

  /**
   * Theme Management
   */
  const initTheme = () => {
    els.themeSelect = document.getElementById('theme-select');
    
    // Load saved or default
    const savedTheme = localStorage.getItem(THEME_KEY) || 'dark';
    applyTheme(savedTheme);

    if (els.themeSelect) {
      els.themeSelect.value = savedTheme;
      els.themeSelect.addEventListener('change', (e) => {
        const theme = e.target.value;
        applyTheme(theme);
        localStorage.setItem(THEME_KEY, theme);
      });
    }
  };

  const applyTheme = (themeName) => {
    if (!AVAILABLE_THEMES.includes(themeName)) return;
    
    // Remove all existing theme classes
    AVAILABLE_THEMES.forEach(t => document.body.classList.remove(`theme-${t}`));
    
    // Default is dark (no specific class needed for dark if base vars are dark, 
    // but applying for consistency if needed, though our base is dark)
    if(themeName !== 'dark') {
        document.body.classList.add(`theme-${themeName}`);
    }
    
    // Dispatch event so tools or 3D scenes can react (e.g. change Three.js colors)
    window.dispatchEvent(new CustomEvent('themechanged', { detail: { theme: themeName } }));
  };

  /**
   * Settings Backup & Restore
   */
  const bindSettingsControls = () => {
    els.btnBackup = document.getElementById('btn-backup');
    els.btnRestore = document.getElementById('btn-restore');
    els.restoreInput = document.getElementById('restore-file-input');

    if (els.btnBackup) {
      els.btnBackup.addEventListener('click', handleBackup);
    }

    if (els.btnRestore && els.restoreInput) {
      els.btnRestore.addEventListener('click', () => els.restoreInput.click());
      els.restoreInput.addEventListener('change', handleRestore);
    }
  };

  const handleBackup = () => {
    try {
      const data = {};
      // Iterate through localStorage and save everything belonging to toolbox
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        // Save everything for this project. In a real app we might prefix keys logic like 'tbx_'
        data[key] = localStorage.getItem(key);
      }
      
      const json = JSON.stringify(data, null, 2);
      const blob = new Blob([json], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      
      const a = document.createElement('a');
      a.href = url;
      a.download = `toolbox-backup-${new Date().toISOString().split('T')[0]}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      
      showToast('Settings backed up successfully!');
    } catch (e) {
      console.error('Backup failed:', e);
      showToast('Failed to backup settings.', 'error');
    }
  };

  const handleRestore = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const data = JSON.parse(event.target.result);
        
        // Merge into localStorage
        Object.keys(data).forEach(key => {
          localStorage.setItem(key, data[key]);
        });
        
        showToast('Settings restored successfully! Reloading...');
        
        // Reset file input
        e.target.value = '';
        
        setTimeout(() => window.location.reload(), 1500);
      } catch (err) {
        console.error('Restore failed:', err);
        showToast('Invalid backup file.', 'error');
      }
    };
    reader.readAsText(file);
  };

  /**
   * UI Helpers
   */
  const showToast = (message, type = 'success') => {
    if (!els.toastContainer) return;
    
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    const icon = type === 'success' ? '✓' : '⚠';
    toast.innerHTML = `<span>${icon}</span> <span>${message}</span>`;
    
    els.toastContainer.appendChild(toast);
    
    // Auto remove
    setTimeout(() => {
      toast.style.animation = 'fadeOut 0.3s ease forwards';
      setTimeout(() => els.toastContainer.removeChild(toast), 300);
    }, 3000);
  };

  return {
    init,
    showToast,
    getTheme: () => localStorage.getItem(THEME_KEY) || 'dark'
  };
})();

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', AppCore.init);
