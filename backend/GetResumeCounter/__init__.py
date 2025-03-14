import logging
import os
import json
import azure.functions as func
import sys
import pkg_resources

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Diagnostic function running to debug modules')
    
    try:
        # Check Python path
        python_path = sys.path
        
        # Check installed packages
        installed_packages = sorted([f"{d.project_name}=={d.version}" 
                               for d in pkg_resources.working_set])
        
        # Check if we have any azure packages
        azure_packages = [p for p in installed_packages if p.startswith('azure')]
        
        # Check the directory content
        dir_content = os.listdir('/home/site/wwwroot')
        
        # Try to inspect `.python_packages` if it exists
        python_pkg_path = '/home/site/wwwroot/.python_packages'
        python_pkg_content = []
        if os.path.exists(python_pkg_path):
            python_pkg_content = os.listdir(python_pkg_path)
            
            # Look deeper
            if 'lib' in python_pkg_content:
                lib_path = os.path.join(python_pkg_path, 'lib')
                lib_content = os.listdir(lib_path)
                python_pkg_content.append(f"lib contents: {lib_content}")
                
                if 'site-packages' in lib_content:
                    site_packages = os.path.join(lib_path, 'site-packages')
                    site_packages_content = os.listdir(site_packages)
                    python_pkg_content.append(f"site-packages contents: {site_packages_content}")
        
        return func.HttpResponse(
            json.dumps({
                "python_path": python_path,
                "installed_packages": installed_packages,
                "azure_packages": azure_packages,
                "directory_content": dir_content,
                "python_packages_content": python_pkg_content
            }, indent=2),
            mimetype="application/json",
            status_code=200
        )
        
    except Exception as e:
        logging.error(f"Diagnostic error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e), "traceback": str(sys.exc_info())}),
            mimetype="application/json",
            status_code=500
        )