const initRoleRadio = () => {
    // Initialize the labels on document load
    window.addEventListener('DOMContentLoaded', (event) => {
        document.querySelectorAll('input[name="role"]:checked').forEach(radio => {
            handleRadioChange(radio);
        });

        document.querySelectorAll('label.role-label').forEach((label) => {
            label.addEventListener('mouseenter', function() {
                this.querySelector('div').classList.add('border-blue-400');
            });
        
            label.addEventListener('mouseleave', function() {
                this.querySelector('div').classList.remove('border-blue-400');
            });
        });
    });
};

const handleRadioChange = (radio) => {
    document.querySelectorAll('.role-label').forEach(label => {
        label.classList.replace('text-gray-700', 'text-gray-400');
        label.querySelector('div').classList.remove('bg-blue-600');
    });

    if (radio.checked) {
        radio.parentElement.classList.replace('text-gray-400', 'text-gray-700');
        radio.nextElementSibling.classList.add('bg-blue-600');
    }
};

const initFormMask = () => {
    var selector = document.getElementById("id_phone");
    var im = new Inputmask("(999) 999-9999");
    im.mask(selector);
};

const initFormDelete = () => {
    let deleteButton = document.getElementById("delete");
    if (!deleteButton) return;
    
    deleteButton.addEventListener('click', function() {
        Swal.fire({
            title: 'Delete Team Member?',
            text: 'Are you sure you want to delete this team member?',
            confirmButtonText: 'Yes',
            showCancelButton: true,
            confirmButtonColor: 'rgb(59 130 246)',
        }).then((result) => {
            if (result.isConfirmed) {
                document.getElementById('input-action').value = 'delete';
                document.getElementById('team-member-form').submit();
            }
        });
  });
};

function initFormSumit() {
    document.addEventListener("DOMContentLoaded", function() {
        const form = document.getElementById('team-member-form');

        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            let valid = true;

            if(document.getElementById('input-action').value === 'delete') {
                form.submit();
                return;
            }

            const field_first_name = document.getElementById('id_first_name');
            const firstName = field_first_name.value.trim();
            if (!firstName) {
            setFieldInvalid(field_first_name, "First name is required.");  
            valid = false;
            }

            const field_last_name = document.getElementById('id_last_name');
            const lastName = field_last_name.value.trim();
            if (!lastName) {
            setFieldInvalid(field_last_name, "Last name is required.");
            valid = false;
            }

            const field_email = document.getElementById('id_email');
            const email = field_email.value.trim();
            if (!email) {
            setFieldInvalid(field_email, "Email is required.");
            valid = false;
            }
            else {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                setFieldInvalid(field_email, "Please enter a valid email address.");
                valid = false;
            }
            }
            
            const field_phone = document.getElementById('id_phone');
            const phone = field_phone.value.trim();
            if (!phone) {
                setFieldInvalid(field_phone, "Phone is required.");
                valid = false;
            }
            else {
                const phoneRegex = /^\(\d{3}\) \d{3}-\d{4}$/;
                if (!phoneRegex.test(phone)) {
                    setFieldInvalid(field_phone, "Phone number must be in the format (999) 999-9999.");
                    valid = false;
                }
            }
            
            if (valid) {
                form.submit();
            }
        });
    });
}

function setFieldInvalid(field, message) {
  field.classList.add('border-red-500', 'bg-red-100');
  field.nextElementSibling.textContent = message;
  field.nextElementSibling.classList.remove('hidden');

  if(!field.classList.contains('event-listener-set')) 
    field.classList.add('event-listener-set');{
    field.addEventListener('input', function() {
      field.classList.remove('border-red-500', 'bg-red-100');
      field.nextElementSibling.textContent = "";
      field.nextElementSibling.classList.add('hidden');
    });
  }
}

const init = () => {
    initRoleRadio();
    initFormMask();
    initFormDelete();
    initFormSumit();
}

init();