from fastapi import APIRouter
from src.controllers.DiscoverController import DiscoverController
from src.validator.agent import ApiResponse

# prefix="/discover",
router = APIRouter(tags=['Discover News agent'])


@router.get('/discover')
def discover():
  return DiscoverController.documentation()
