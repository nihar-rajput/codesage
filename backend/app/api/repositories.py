from fastapi import APIRouter
from app.services.git_service import GitService
from app.schemas.repository import CloneRepositoryRequest

router = APIRouter(prefix="/repositories",
                   tags=["Repositories"])

@router.post("/clone")
def clone(request : CloneRepositoryRequest ):
    service = GitService()
    destination = service.clone_repository(request.url)
    return {
        "message": "Repository cloned successfully",
        "path": str(destination)
    }