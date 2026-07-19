from fastapi import APIRouter
from fastapi import HTTPException
from app.services.git_service import GitService
from app.schemas.repository import CloneRepositoryRequest

router = APIRouter(prefix="/repositories",
                   tags=["Repositories"])

@router.post("/clone")
def clone(request : CloneRepositoryRequest ):
    service = GitService()
    try:
        destination = service.clone_repository(request.url)
        return {
            "message": "Repository cloned successfully",
            "path": str(destination)
        }
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    except FileExistsError as e:
        raise HTTPException(status_code=409,detail=str(e))