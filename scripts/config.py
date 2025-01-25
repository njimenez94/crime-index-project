import os


def setup_paths():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio donde se ejecuta el script
    project_root = os.path.abspath(os.path.join(current_dir, '..'))  # Subir un nivel al directorio raíz del proyecto
    
    return {
        'data_raw': os.path.join(project_root, 'data', 'raw'),
        'data_processed': os.path.join(project_root, 'data', 'processed'),
        'results_figures_images': os.path.join(project_root, 'results', 'figures', 'images'),
        'results_figures_html': os.path.join(project_root, 'results', 'figures', 'html'),
        'results_tables': os.path.join(project_root, 'results', 'tables')
    }
