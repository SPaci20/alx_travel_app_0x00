from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for Listing model
    """
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'available', 'created_at']
        read_only_fields = ['id', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model
    """
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'listing_title', 'guest_name', 'check_in', 'check_out', 'created_at']
        read_only_fields = ['id', 'created_at']
        
    def validate(self, data):
        """
        Check that check_out is after check_in
        """
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError("Check-out date must be after check-in date.")
        return data
